import json
from django import http
from api.models import Profiles, Users
from channels import layers
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from asgiref.sync import async_to_sync
from django.core.serializers import serialize



def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def room(request, first, second):
    return render(request, 'room.html', {
        'first': first,
        'second': second
    })
    
def  emojis(request):
    if request.method == "GET":
        emojis = list(Emoji.objects.values().values_list('emoji',flat=True))
        data = {}
        data['error'] = False
        data['success_msg'] = 'Successfully emojis retrieved'
        data['emojis'] = emojis
        return JsonResponse(data,safe=False)
    else:
        data = {}
        data['error'] = True
        data['error_msg'] = 'Method not supported'    
        return JsonResponse(data)
    
def  gifts(request):
    if request.method == "GET":
        gifts = list(Gifts.objects.values().values_list('gift',flat=True))
        data = {}
        data['error'] = False
        data['success_msg'] = 'Successfully GIF retrieved'
        data['gifts'] = gifts
        return JsonResponse(data,safe=False)
    else:
        data = {}
        data['error'] = True
        data['error_msg'] = 'Method not supported'    
        return JsonResponse(data)
    
    
def notifications(request):
    return render(request, 'video/index.html')

    
def sendnotifications(request):
    user = list(Users.objects.filter(id=1).values('id', 'name', 'email'))[0]
    profile = list(Profiles.objects.filter(user_id=1).values('id', 'user_id', 'image'))[0]
    user['profile'] = profile
    group_data = list(Groups.objects.filter(id=2).values('id'))[0]
    group_data['user'] = user
    group_data['chat_id'] = 245
    group_data['status'] = 'calling'
    layer = layers.get_channel_layer()
    async_to_sync(layer.group_send)('notification_1', {
           'type': 'chat_message',
           'data': group_data
        })
    return HttpResponse('ok')

