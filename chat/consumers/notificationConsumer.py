import json
import uuid
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from chat.models import Groups, Chat
from api.models import Users
from django.db.models import Q 
from uuid import uuid4
import base64
from django.core.files.base import ContentFile


class NotificationConsumer(WebsocketConsumer):
    status = ''
    # def __init__(self, *args, **kwargs):
        # self.user_id = 1
        # self.connect()
    
    def connect(self, user_id=None):
        try:
            self.user_id = self.scope['url_route']['kwargs']['user_id']
                
            userExists = self.checkUserExists()
            if userExists:
                self.room_group_name = 'notification_'+str(userExists.id)
                async_to_sync(self.channel_layer.group_add)(
                    self.room_group_name,
                    self.channel_name
                )
                self.accept()
            else:
                pass
        except Exception as e:
            print('In Exception Noti Connect')
            print(e)

    

    # Receive message from WebSocket
    def receive(self, text_data):
        try:
            data =  text_data
            self.status = data['status']
            if data['status'] == 'calling':
                pass
            async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'data': data
                    }
                )
        except Exception as e:
            print(e)
                    

    # Receive message from room group
    def chat_message(self, event):
        try:
            data = event['data']
            self.send(text_data= json.dumps(data))
            # Send message to WebSocket
        except Exception as e:
            print(e)    
        
    def checkUserExists(self):
        query = Users.objects.filter(id=self.user_id).first()
        return query
    
    
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )