from adminn.models import Auto_msg, Message
from api.models import Users, Profiles
from chat.models import Groups, Chat
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from chat.consumers.consumers import ChatConsumer

@csrf_exempt
def getGroups(request):
    user_id = request.POST['user_id']
    groups = getUserGroups(user_id)
    admin_messages =[]
    last_message={}
    if Message.objects.all().exists():
        l_message= list(Message.objects.all().order_by('-id').values('message'))[0]
        last_message ['last_message']= l_message['message']
        l_message_date=list(Message.objects.all().order_by('-id').values('created_at'))[0]
        last_message['last_message_date']=l_message_date['created_at']
        last_message['chat'] = list(Message.objects.all().values('id','message','created_at'))
        admin_messages.append(last_message)
    return JsonResponse({'error': False, 'success_msg': 'Contacts Retrieved!','admin_messages':admin_messages,'groups': groups})

@csrf_exempt
def createGroup(request):
    user1 = request.POST['user1']
    user2 = request.POST['user2']
    
    groupExists = checkGroupExists(user1, user2)
    if not groupExists:
        group = Groups()
        group.user_first=user1  
        group.user_second=user2
        group.status=True
        group.save()
        return JsonResponse({'error': False, 'success_msg': 'Room Created Successfully!', 'room_id': group.pk})
    else:
        return JsonResponse({'error': False, 'success_msg': 'Room Already Created!', 'room_id': groupExists.id})

@csrf_exempt
def getChat(request):
    group_id = request.POST.get('group_id')
    user_id = request.POST.get('user_id')
    groupExists = checkGroupExistsById(group_id)
    if groupExists:
        chats = list(Chat.objects.filter(group_id=groupExists.id).exclude(Q(deleted_by_user1=user_id) | Q(deleted_by_user2=user_id) | Q(delete_chat_by_user1=user_id) | Q(delete_chat_by_user2=user_id)).order_by('id').values())
        auto_msg = Auto_msg.objects.filter(id=1).first()
        greetings = auto_msg.matching
        return JsonResponse({'error': False, 'success_msg': 'Chat Retrieved!','greetings':greetings, 'chat': chats})
    else:
        auto_msg = Auto_msg.objects.filter(id=1).first()
        greetings = auto_msg.matching
        return JsonResponse({'error': False, 'success_msg': 'Chat Retrieved!','greetings':greetings, 'chat': []})

@csrf_exempt
def updateChat(request):
    group_id = request.POST['group_id']
    chat_id = request.POST['chat_id']
    message = request.POST['message']
    chat = Chat.objects.filter(id=chat_id,group_id=group_id).first()
    if chat:
        chat.message = message
        chat.save()
        data={}
        data['error'] = False
        data['success_msg'] = 'Successfully updated'
        return JsonResponse(data)
    else:
        data={}
        data['error'] = True
        data['success_msg'] = 'Chat does not exist'
        return JsonResponse(data)

@csrf_exempt
def delete_msg_everyone(request):
    group_id = request.POST['group_id']
    chat_id = request.POST['chat_id']
    user_id = request.POST['user_id']
    chat = Chat.objects.filter(id=chat_id,group_id=group_id,sender=user_id).first()
    if chat:
        reciever_id = chat.receiver
        chat.deleted_by_user1 = user_id
        chat.deleted_by_user2 = reciever_id
        chat.save()
        data={}
        data['error'] = False
        data['success_msg'] = 'Successfully deleted'
        return JsonResponse(data)
    else:
        data={}
        data['error'] = True
        data['error_msg'] = 'Chat does not exist'
        return JsonResponse(data)
    
@csrf_exempt
def delete_msg_onlyme(request):
    group_id = request.POST['group_id']
    chat_id = request.POST['chat_id']
    user_id = request.POST['user_id']
    chat = Chat.objects.filter(id=chat_id,group_id=group_id,sender=user_id).first()
    if chat:
        chat.deleted_by_user1 = user_id
        chat.save()
        data={}
        data['error'] = False
        data['success_msg'] = 'Successfully deleted'
        return JsonResponse(data)
    else:
        data={}
        data['error'] = True
        data['error_msg'] = 'Chat does not exist'
        return JsonResponse(data)
    
    
@csrf_exempt
def delete_chat(request):
    group_id = request.POST['group_id']
    user_id = request.POST['user_id']
    chats = Chat.objects.filter(group_id=group_id).all()
    if chats:
        for chat in chats: 
            if chat.delete_chat_by_user1 == 0:
                chat.delete_chat_by_user1 = user_id
                chat.save()
            elif chat.delete_chat_by_user2 == 0 and chat.delete_chat_by_user1 != int(user_id):
                chat.delete_chat_by_user2 = user_id
                chat.save()
        data={}
        data['error'] = False
        data['success_msg'] = 'Successfully deleted'
        return JsonResponse(data)
    else:
        data={}
        data['error'] = True
        data['error_msg'] = 'Chat does not exist'
        return JsonResponse(data)
    
    
@csrf_exempt
def seenChat(request):
    group_id = request.POST.get('group_id')
    user_id = request.POST.get('user_id')
    chats = Chat.objects.filter(group_id=group_id).order_by('-id')
    last_id = Chat.objects.last().sender
    if chats:
        if last_id != int(user_id):
            for chat in chats:
                chat.seen = True
                chat.save()
            sendNotification(user_id)
            return JsonResponse({'error': False, 'success_msg': 'Messages seen!'})
        else:
            return JsonResponse({'error': False, 'success_msg': 'Messages all already seen!'})
    else:
        return JsonResponse({'error': False, 'success_msg': 'Messages all already seen!'})

def checkGroupExists(user1, user2):
    query = Groups.objects.filter(Q(user_first=user1, user_second=user2) | Q(user_first=user2, user_second=user1)).first()
    return query


def checkGroupExistsById(group_id):
    query = Groups.objects.filter(id=group_id).first()
    return query

def getUserGroups(user_id):
    data = []
    groups = list(Groups.objects.filter(Q(user_first=user_id,instant_msg_status=True) | Q(user_second=user_id,instant_msg_status=True)).values())
    if len(groups) > 0:
        for group in groups:
            other_user_id = int(group['user_first'])
            if int(group['user_first']) == int(user_id):
                other_user_id = int(group['user_second'])
            otherUser = list(Users.objects.filter(id=other_user_id).values())
            if len(otherUser):
                otherUser = otherUser[0]
                OtherUserprofile = list(Profiles.objects.filter(user_id=otherUser['id']).values())[0]
                otherUser['profile'] = OtherUserprofile
                last_message = list(Chat.objects.filter(group_id=group['id']).exclude(Q(deleted_by_user1=user_id) | Q(deleted_by_user2=user_id) | Q(delete_chat_by_user1=user_id) | Q(delete_chat_by_user2=user_id)).order_by('-created_at')[:1].values())
                if len(last_message) > 0:
                    if last_message[0]['message']:
                        group['last_message'] = last_message[0]['message'].upper()
                    elif last_message[0]['image']:
                        group['last_message'] = 'IMAGE'
                    elif last_message[0]['voice']:
                        group['last_message'] = 'VOICE'
                    elif last_message[0]['svg']:
                        group['last_message'] = 'STICKER'
                    elif last_message[0]['call_status'] == 0 or last_message[0]['call_status']:
                        group['last_message'] = 'CALL LOG'
                    elif last_message[0]['address']:
                        group['last_message'] = 'MEETING LINK'
                    else:
                        group['last_message'] = ''
                else:
                    group['last_message'] = ''
                group['last_message_date'] = last_message[0]['created_at'] if len(last_message) > 0 else group['created_at']
                unseen_message = Chat.objects.filter(group_id=group['id'],seen=0,receiver=user_id).count()           
                group['unseen_message'] = unseen_message
                if group['status'] == 1:
                    group['matching_status'] = 1
                else:
                    group['matching_status'] = 0
                if group['blocked_by_user'] == int(user_id):
                    group['block_status'] = 1
                else:
                    group['block_status'] = 0 
                if group['unblock_by_user'] == int(user_id):
                    group['block_status'] = 2
                group['user'] = otherUser 
                data.append(group)
    return data

def sendNotification(receiver_id):
    layer = get_channel_layer()
    group_name = 'notification_'+str(receiver_id)
    msg_count = getUserUnSeenChatCount(receiver_id)
    async_to_sync(layer.group_send)(group_name, {
        'type': 'chat_message',
        'data': {"status": "message", "msg_count": msg_count}
        })
    
def getUserUnSeenChatCount(user_id):
    groups = Groups.objects.filter(Q(user_first=user_id) | Q(user_second=user_id)).values_list('id', flat=True)
    chats_count = Chat.objects.filter(group_id__in=groups, seen=False, receiver=user_id).values_list('group_id', flat=True).distinct().count()
    return str(chats_count)