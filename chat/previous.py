import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.dispatch.dispatcher import receiver
from chat.models import Groups, Chat
from django.contrib.auth.models import User
from django.db.models import Q 
from uuid import uuid4
import base64
from django.core.files.base import ContentFile


class ChatConsumer(WebsocketConsumer):
    # def __init__(self):
    #     self.status = 'typing'
    
    def connect(self):
        # self.first = self.scope['url_route']['kwargs']['first']
        # self.second = self.scope['url_route']['kwargs']['second']

        # groupExists = self.checkGroupExists()
        # if groupExists:
        #     self.room_group_name = str(groupExists.id)
        
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
            self.accept()
        # else:
        #     pass

    

    # Receive message from WebSocket
    def receive(self, text_data):
        data =  json.loads(text_data)
        data = data['data']
        print('channel py message aya')
        # Storing Chat message
        self.status = 'typing'
                
        typing = True if data['typing'] == True else False
        if not typing:
            
            # Seen Message
            seen = True if data['seen'] == True else False
            if seen:
                self.status = 'seen'
                chat = Chat.objects.filter(id=data['chat_id']).first()
                if chat:
                    chat.seen = True
                    chat.save()
            else:
                self.status = 'message' 
                
                #save message 
                group = Groups.objects.get(id=data['group'])
                if data['image'] or data['image'].strip() != '':
                    image = self.base64_to_image(data['image'])
                    chat = Chat(sender=data['sender'], receiver=data['receiver'],image=image,message=None,group=group)
                    chat.save()
                    data['id'] = chat.pk
                    self.chat_id = chat.pk
                # elif data['video'] or data['video'].strip() != '':
                #     video = self.self.base64_to_image(data['video'])
                #     chat = Chat(sender=data['sender'], receiver=data['receiver'],video=video,message=None,image=None,group=group)
                #     chat.save()
                #     data['id'] = chat.pk
                #     self.chat_id = chat.pk
                else:
                    chat = Chat(sender=data['sender'], receiver=data['receiver'], message=data['message'],image=None,group=group)
                    chat.save()
                    data['id'] = chat.pk
                    self.chat_id = chat.pk
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'data': data
            }
        )
                

    # Receive message from room group
    def chat_message(self, event):
        data = event['data']
        
        if self.status == 'message':
            data['id'] = self.chat_id
        # Send message to WebSocket
        print('channel sy message gya')

        self.send(text_data=json.dumps({
            'data': data
        }))
        
    def checkGroupExists(self):
        query = Groups.objects.filter(Q(user_first=self.first, user_second=self.second) | Q(user_first=self.second, user_second=self.first)).first()
        return query
    
    
    def disconnect(self, close_code):
        print(close_code)
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    
    def base64_to_image(base64_string):
        format, imgstr = base64_string.split(';base64,') 
        ext = format.split('/')[-1]
        return ContentFile(base64.b64decode(imgstr), name=uuid4().hex + "." + ext)