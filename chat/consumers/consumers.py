import json
import re
import requests
from api.models import Users
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from chat.models import Groups, Chat
from django.db.models import Q 
from uuid import uuid4
import base64
from django.core.files.base import ContentFile
from django.db.models import Q
from django.core import serializers
from api.notifications import sendPushNotification
from datetime import datetime




class ChatConsumer(WebsocketConsumer):
    status = ''
    
    def connect(self):
        try:
            self.first = self.scope['url_route']['kwargs']['first']
            self.second = self.scope['url_route']['kwargs']['second']

            groupExists = self.checkGroupExists()
            if groupExists:
                self.room_group_name = str(groupExists.id)
            
                async_to_sync(self.channel_layer.group_add)(
                    self.room_group_name,
                    self.channel_name
                )
                self.accept()
                print('connected')
            else:
                pass
        except Exception as e:
            print(e)

    

    # Receive message from WebSocket
    def receive(self, text_data):
        try:
            data =  json.loads(text_data)
            self.status = data['status']
            
            if data['status'] == 'typing':
                pass    
            if data['status'] == 'all_seen':
                pass 
            if data['status'] == 'single_delete':
                pass            
            if data['status'] == 'seen':
                chat = Chat.objects.filter(id=data['chat_id']).first()
                if chat:
                    chat.seen = True
                    chat.save()
           
            if data['status'] == 'message':
                self.status = 'message'
                group = Groups.objects.get(id=data['group_id'])
                if data['image']:
                    image = self.base64_to_image(data['image'])
                    chat = Chat(sender=data['sender'], receiver=data['receiver'],image=image,message=None,group=group)
                    chat.save()
                    data['id'] = chat.pk
                    self.chat_id = chat.pk
                    self.chat_date = chat.created_at
                elif data['voice']:
                    # print(data['voice'])
                    # voice = self.base64_to_voice(data['voice'])
                    format, imgstr = data['voice'].split(';base64,') 
                    for i in range(1, 100):
                        if (len(imgstr) % 4) == 0:
                            break
                        imgstr += 'A'
                    ext = format.split('/')[-1] 
                    fileName = str(uuid4().hex) + "." + str(ext)
                    voice = ContentFile(base64.b64decode(imgstr), name=fileName )
                    current_time = datetime.now().strftime('%H:%M:%S')   
                    chat = Chat(sender=data['sender'], receiver=data['receiver'],voice=voice,message=None,image=None,time=current_time,group=group)
                    chat.save()
                    data['id'] = chat.pk
                    self.chat_id = chat.pk
                    self.chat_date = chat.created_at
                elif data['svg']:
                    chat = Chat(sender=data['sender'], receiver=data['receiver'],image=None,svg=data['svg'],message=None,voice=None,group=group)
                    chat.save()
                    data['id'] = chat.pk
                    self.chat_id = chat.pk
                    self.chat_date = chat.created_at               
                elif data['message']:
                    chat = Chat(sender=data['sender'], receiver=data['receiver'], message=data['message'],image=None,voice=None,group=group)
                    chat.save()
                    data['id'] = chat.pk
                    self.chat_id = chat.pk
                    self.chat_date = chat.created_at
                elif data['address']:
                    chat = Chat(sender=data['sender'], receiver=data['receiver'], address=data['address'],latitude=data['latitude'],longitude=data['longitude'],date=data['date'],time=data['time'],image=None,group=group)
                    chat.save()
                    data['id'] = chat.pk
                    self.chat_id = chat.pk
                    self.chat_date = chat.created_at
                    
                # Send Notifications
                self.sendNotification(data['receiver'], data['sender'])
            
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'data': data
                }
            )
        except Exception as e:
            print('Exception')
            print(e)
                    

    # Receive message from room group
    def chat_message(self, event):
        try:
            data = event['data']
            if self.status == 'message':
                data['id'] = self.chat_id
                data['created_at'] = str(self.chat_date)
                self.send(text_data= json.dumps(data))
            else:
                self.send(text_data= json.dumps(data))
                
            # Send message to WebSocket
        except Exception as e:
            print("//////////EXCEPTION///////////")
            print(e)    
        
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
    
    def base64_to_image(self, base64_string):
        format, imgstr = base64_string.split(';base64,') 
        ext = format.split('/')[-1]
        return ContentFile(base64.b64decode(imgstr), name=uuid4().hex + "." + ext)
    
    def base64_to_voice(self, base64_string):
        format, imgstr = base64_string.split(';base64,') 
        for i in range(1, 100):
            if (len(imgstr) % 4) == 0:
                break
            imgstr += 'A'
        ext = format.split('/')[-1] 
        fileName = str(uuid4().hex + "." + ext)
        return ContentFile(base64.b64decode(imgstr), name=fileName ) # You can save this as file instance.
    
    
    def sendNotification(self, receiver_id, sender_id):        
        layer = get_channel_layer()
        group_name = 'notification_'+str(receiver_id)
        msg_count = self.getUserGroups(receiver_id)
        async_to_sync(layer.group_send)(group_name, {
            'type': 'chat_message',
            'data': {"status": "message", "msg_count": msg_count}
            })
        # Send Notification
        sendPushNotification(sender_id, receiver_id, type='Message')
        
    # def getUserGroups(self, user_id):
    #     groups = Groups.objects.filter(Q(user_first=user_id) | Q(user_second=user_id)).values_list('id', flat=True)
    #     chats_count = Chat.objects.filter(group_id__in=groups, seen=False, receiver=user_id).count()
    #     return str(chats_count)
    
    def getUserGroups(self,user_id):
        groups = Groups.objects.filter(Q(user_first=user_id) | Q(user_second=user_id)).values_list('id', flat=True)
        chats_count = Chat.objects.filter(group_id__in=groups, seen=False, receiver=user_id).values_list('group_id', flat=True).distinct().count()
        return str(chats_count)