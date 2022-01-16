import os
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt   
from pyfcm import FCMNotification
from dotenv import load_dotenv

from api.models import Users
load_dotenv()

def sendPushNotification(sender_id, receiver_id, type):
    # push_service = FCMNotification(api_key=os.getenv("fcm_server_key"),)
    sender = Users.objects.get(id=sender_id)
    receiver = Users.objects.get(id=receiver_id)
    subject = 'Serious Dating Notification'
    title = ''
    message = ''
    if type == 'Match':
        title = 'Match'
        message = 'You Have Matched With '+ str(sender.name)
    elif type == 'Like':
        title = 'Like'
        message = str(sender.name)+ ' Liked You!'
    elif type == 'Message':
        title = 'Message'
        message = 'Received a message from '+ str(sender.name)
    elif type == 'Call':
        title = 'Call'
        message = str(sender.name) + ' Is Calling You!'

    registration_id = receiver.expo_token
    # extra_notification_kwargs = {}
    if registration_id:
        API_ENDPOINT = "https://exp.host/--/api/v2/push/send"
        data = {
        'to': registration_id,
        'sound': 'default',
        'title': title,
        'body': message}
        r = requests.post(url = API_ENDPOINT, data = data)
        # pastebin_url = r.text
        # print("The pastebin URL is:%s"%pastebin_url)
        # return HttpResponse(r)
        # result = push_service.notify_single_device(registration_id=registration_id, message_title=subject, message_body=message)
    else:
        print('Device Token Not Handled!')

def pushtest():
    push_service = FCMNotification(api_key=os.getenv("fcm_server_key"),)
    registration_id = 'dQpVHYjeRJWFgPFsf2fA16:APA91bHqBa3G-ffCTANta49my02_SQs02-mf6VLOwYazNmL0VFUfe_MGzH9k5rDTFcVXUX1nxRglx7xFFQaVdTu5yfwjdYlkwOGH7ybhryUGrarn0YzyzVU7l5jD3tmkJQpZ4evfxTpG'
    extra_notification_kwargs = {}
    if registration_id:
        print("/////////////////////////TEST NOTIFICATION//////////////////////")
        result = push_service.notify_single_device(registration_id=registration_id, message_title='subject', message_body='message')
        print(result)
    else:
        print("/////////////////////////TEST NOTIFICATION//////////////////////")
        print('Device Token Not Handled!')



# importing the requests library
import requests
@csrf_exempt
def Test_Noti(request):
    # defining the api-endpoint
    API_ENDPOINT = "https://exp.host/--/api/v2/push/send"

    # data to be sent to api
    data = {
    # 'to': 'ExponentPushToken[-x1LMuAGNJa8V1-vosJ3NP]',
    'to': 'ExponentPushToken[FEm5yiLRm77DKTVxdO9nKW]',
    'sound': 'default',
    'title': 'Original Title',
    'body': 'And here is the body!'}

    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = data)

    # extracting response text
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)
    return HttpResponse(r)
