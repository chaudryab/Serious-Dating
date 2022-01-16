from django.urls import re_path

from .consumers import consumers, videoConsumers, notificationConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<first>\w+)/(?P<second>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/video/(?P<group_id>\w+)/$', videoConsumers.VideoConsumer.as_asgi()),
    re_path(r'ws/notifications/(?P<user_id>\w+)/$', notificationConsumer.NotificationConsumer.as_asgi()),
    # re_path(r'ws/websocket.connect/', notificationConsumer.NotificationConsumer.ws_connect),
    # re_path(r'ws/websocket.disconnect/', notificationConsumer.NotificationConsumer.ws_disconnect),
]