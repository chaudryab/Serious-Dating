import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from chat.models import Groups, Chat
from api.models import Users, Profiles
from django.db.models import Q 
from uuid import uuid4
import base64

from api.notifications import sendPushNotification
from .notificationConsumer import NotificationConsumer
from django.core.files.base import ContentFile
from django.core.serializers import serialize
import requests

class VideoConsumer(WebsocketConsumer):
    status = ''
    
    def connect(self):
        try:
            self.group_id = self.scope['url_route']['kwargs']['group_id']

            groupExists = self.checkGroupExists()
            if groupExists:
                self.room_group_name = str(groupExists.id)
                async_to_sync(self.channel_layer.group_add)(
                    self.room_group_name,
                    self.channel_name
                )
                self.accept()
            else:
                pass
        except Exception as e:
            print(e)

    

    # Receive message from WebSocket
    def receive(self, text_data):
        try:
            data =  json.loads(text_data)
            self.status = data['status']
            print(data)
            
            if data['status'] == 'calling':
                chat = Chat()
                chat.call_type = 0 # calling 1 ringing 2 accepting 3 canceled 4 rejected 5 
                chat.sender = data['sender']
                chat.receiver = data['receiver']
                chat.group_id = data['group_id']
                chat.call_status = data['call_status']
                chat.ended_by = 0
                chat.save()
                self.chat_id = chat.pk
                user = list(Users.objects.filter(id=data['sender']).values('id', 'name', 'email'))[0]
                profile = list(Profiles.objects.filter(user_id=data['sender']).values('id', 'user_id', 'image'))[0]
                user['profile'] = profile
                group_data = list(Groups.objects.filter(id=data['group_id']).values('id'))[0]
                # chat = list(Chat.objects.filter(id=self.chat_id).values())[0]
                group_data['user'] = user
                group_data['chat_id'] = self.chat_id
                group_data['status'] = 'Video' if data['call_status'] == 1 else 'Audio'
                
                # sending notification to receiver
                self.sendNotification(data['sender'], data['receiver'], group_data)
                
            if data['status'] == 'ringing':
                chat_id = data['id']
                chat = Chat.objects.get(id=chat_id)
                chat.call_type = 1
                chat.save()
            if data['status'] == 'accepting':
                chat_id = data['id']
                chat = Chat.objects.get(id=chat_id)
                chat.call_type = 3
                chat.save()
            if data['status'] == 'rejecting':
                chat_id = data['id']
                chat = Chat.objects.get(id=chat_id)
                chat.call_type = 4
                chat.ended_by = data['ended_by']
                chat.save()
            if data['status'] == 'canceled':
                chat_id = data['id']
                chat = Chat.objects.get(id=chat_id)
                chat.call_type = 5
                chat.ended_by = data['ended_by']
                chat.save()
            if data['status'] == 'missed':
                chat_id = data['id']
                chat = Chat.objects.get(id=chat_id)
                chat.call_type = 6
                chat.save()
            
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'data': data
                }
            )
        except Exception as e:
            print('In Exception')
            print(e)
                    

    # Receive message from room group
    def chat_message(self, event):
        try:
            data = event['data']
            if(data['status'] == 'calling'):
                data['chat_id'] = self.chat_id
            print('before send')
            print(data)
            self.send(text_data= json.dumps(data))
            
            # if self.status == 'message':
            #     data['id'] = self.chat_id
            #     data['created_at'] = str(self.chat_date)
            #     self.send(text_data= json.dumps(data))
            # else:
                # self.send(text_data= json.dumps(data))
                
            # Send message to WebSocket
        except Exception as e:
            print(e)    
        
    def checkGroupExists(self):
        query = Groups.objects.filter(id=self.group_id).first()
        return query
    
    
    def disconnect(self, close_code):
        print(close_code)
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        
    def sendNotification(self, sender_id, receiver_id, group_data):
        # data = serialize("json", [data])
        layer = get_channel_layer()
        group_name = 'notification_'+str(receiver_id)
        async_to_sync(layer.group_send)(group_name, {
            'type': 'chat_message',
            'data': group_data
            })
        # Send Notification
        sendPushNotification(sender_id, receiver_id, type='Call')

        # receiver = Users.objects.get(id=receiver_id)
        # if receiver.expo_token:
        #     params = {'to': receiver.expo_token, 'sound': 'default', 
        #               'title': 'Serious Dating Notification', 
        #               'body': 'Call from '+ group_data['user']['name'], 
        #               'data': group_data }
        #     requests.post('https://exp.host/--/api/v2/push/send', json=params)