from django.urls import path

from . import views
from .chatViews import *

urlpatterns = [
    path('get-groups', getGroups),
    path('create-group', createGroup),
    path('get-chat', getChat),
    path('seen-chat', seenChat),
    path('update-chat', updateChat),
    path('delete-msg-everyone',delete_msg_everyone),
    path('delete-msg-onlyme',delete_msg_onlyme),
    path('delete-chat',delete_chat),
    
    # path('delete-chat', deleteChat),
    # path('send-message', sendMessage),
    path('<int:first>/<int:second>/', views.room, name='room'),
    path('notifications/', views.notifications, name='notifications'),
    path('sendnotifications/', views.sendnotifications, name='sendnotifications'),
    
    
    path('emojis',views.emojis,name='emojis'),
    path('gifts',views.gifts,name='gifts'),
    # path('delete_chat',views.delete_chat,name='delete_chat'),
]