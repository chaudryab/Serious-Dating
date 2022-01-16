from time import strptime
from adminn.models import Auto_msg
from chat.models import Groups
from django.http.response import HttpResponse, JsonResponse
from .models import *
from adminn.models import *
from django.views.decorators.csrf import csrf_exempt
from .helpers import *
import base64
from django.core.files.base import ContentFile
from uuid import uuid4
from django.db.models import Q
import random
from datetime import datetime, timedelta
import re
import requests
from datetime import date
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
from django.shortcuts import render, redirect
from .notifications import sendPushNotification, pushtest
from math import sin, cos, sqrt, atan2, radians



# Create your views here.

#------------- Check Email Exist --------------
@csrf_exempt
def email_exist(request):
    if request.method == "POST":
        email = request.POST['email'].lower()
        user = Users.objects.filter(email=email).first()
        check_user = Users.objects.filter(email=email).first()
        if user:
            if check_user.facebook_key:
                    user = list(Users.objects.filter(email=email).values())[0]
                    data = {}
                    data['error'] = False
                    data['status'] = 'registered'
                    data['success_msg'] = 'Complete your profile!'
                    profile = list(Profiles.objects.filter(user_id=user['id']).values())
                    if len(profile) > 0:
                        data['status'] = 'completed'
                        data['success_msg'] = 'loggedIn successfully!'
                        user['profile'] = profile[0]
                        photo = []
                        user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('id','image'))[0]
                        photo.append(user_profile_img)
                        images = list(Photos.objects.filter(user_id=user['id']).values('id','image'))
                        if images:
                            for i in [0,1,2,3]:
                                if i < len(images):
                                    photo.append(images[i])
                                else:
                                    photo.append({})
                        else:
                            for i in [0,1,2,3]:
                                photo.append({})
                        user['images'] = photo
                    data['user'] = user
                    return JsonResponse(data, safe=False)
            elif check_user.google_key:
                user = list(Users.objects.filter(email=email).values())[0]
                data = {}
                data['error'] = False
                data['status'] = 'registered'
                data['success_msg'] = 'Complete your profile!'
                profile = list(Profiles.objects.filter(user_id=user['id']).values())
                if len(profile) > 0:
                    data['status'] = 'completed'
                    data['success_msg'] = 'loggedIn successfully!'
                    user['profile'] = profile[0]
                    photo = []
                    user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('id','image'))[0]
                    photo.append(user_profile_img)
                    images = list(Photos.objects.filter(user_id=user['id']).values('id','image'))
                    if images:
                        for i in [0,1,2,3]:
                            if i < len(images):
                                photo.append(images[i])
                            else:
                                photo.append({})
                    else:
                        for i in [0,1,2,3]:
                            photo.append({})
                    user['images'] = photo
                data['user'] = user
                return JsonResponse(data, safe=False)
            else:
                user = list(Users.objects.filter(email=email).values())[0]
                data = {}
                data['error'] = False
                data['status'] = 'registered'
                data['success_msg'] = 'Complete your profile!'
                profile = list(Profiles.objects.filter(user_id=user['id']).values())
                if len(profile) > 0:
                    data['status'] = 'completed'
                    data['success_msg'] = 'loggedIn successfully!'
                    user['profile'] = profile[0]
                    photo = []
                    user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('id','image'))[0]
                    photo.append(user_profile_img)
                    images = list(Photos.objects.filter(user_id=user['id']).values('id','image'))
                    if images:
                        for i in [0,1,2,3]:
                            if i < len(images):
                                photo.append(images[i])
                            else:
                                photo.append({})
                    else:
                        for i in [0,1,2,3]:
                            photo.append({})
                    user['images'] = photo
                data['user'] = user
                return JsonResponse(data, safe=False)
        else:
            data = {}
            data['error'] = False
            data['status'] = 'not registered'
            data['success_msg'] = 'Email not found'    
            return JsonResponse(data)
    else:
        data = {}
        data['error'] = True
        data['error_msg'] = 'Method not supported'    
        return JsonResponse(data)

#------------- Check Phone No Exist --------------
@csrf_exempt
def phone_exist(request):
    if request.method == "POST":
        phone = request.POST['phone']
        print('///////////////////')
        print(phone)
        user = Users.objects.filter(phone=phone).first()
        check_user = Users.objects.filter(phone=phone).first()
        if user:
            if check_user.facebook_key:
                    user = list(Users.objects.filter(phone=phone).values())[0]
                    data = {}
                    data['error'] = False
                    data['status'] = 'registered'
                    data['success_msg'] = 'Complete your profile!'
                    profile = list(Profiles.objects.filter(user_id=user['id']).values())
                    if len(profile) > 0:
                        data['status'] = 'completed'
                        data['success_msg'] = 'loggedIn successfully!'
                        user['profile'] = profile[0]
                        photo = []
                        user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('id','image'))[0]
                        photo.append(user_profile_img)
                        images = list(Photos.objects.filter(user_id=user['id']).values('id','image'))
                        if images:
                            for i in [0,1,2,3]:
                                if i < len(images):
                                    photo.append(images[i])
                                else:
                                    photo.append({})
                        else:
                            for i in [0,1,2,3]:
                                photo.append({})
                        user['images'] = photo
                    data['user'] = user
                    return JsonResponse(data, safe=False)
            elif check_user.google_key:
                user = list(Users.objects.filter(phone=phone).values())[0]
                data = {}
                data['error'] = False
                data['status'] = 'registered'
                data['success_msg'] = 'Complete your profile!'
                profile = list(Profiles.objects.filter(user_id=user['id']).values())
                if len(profile) > 0:
                    data['status'] = 'completed'
                    data['success_msg'] = 'loggedIn successfully!'
                    user['profile'] = profile[0]
                    photo = []
                    user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('id','image'))[0]
                    photo.append(user_profile_img)
                    images = list(Photos.objects.filter(user_id=user['id']).values('id','image'))
                    if images:
                        for i in [0,1,2,3]:
                            if i < len(images):
                                photo.append(images[i])
                            else:
                                photo.append({})
                    else:
                        for i in [0,1,2,3]:
                            photo.append({})
                    user['images'] = photo
                data['user'] = user
                return JsonResponse(data, safe=False)
            else:
                user = list(Users.objects.filter(phone=phone).values())[0]
                data = {}
                data['error'] = False
                data['status'] = 'registered'
                data['success_msg'] = 'Complete your profile!'
                profile = list(Profiles.objects.filter(user_id=user['id']).values())
                if len(profile) > 0:
                    data['status'] = 'completed'
                    data['success_msg'] = 'loggedIn successfully!'
                    user['profile'] = profile[0]
                    photo = []
                    user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('id','image'))[0]
                    photo.append(user_profile_img)
                    images = list(Photos.objects.filter(user_id=user['id']).values('id','image'))
                    if images:
                        for i in [0,1,2,3]:
                            if i < len(images):
                                photo.append(images[i])
                            else:
                                photo.append({})
                    else:
                        for i in [0,1,2,3]:
                            photo.append({})
                    user['images'] = photo
                data['user'] = user
                return JsonResponse(data, safe=False)
        else:
            data = {}
            data['error'] = False
            data['status'] = 'not registered'
            data['success_msg'] = 'Phone Number not found'    
            return JsonResponse(data)
    else:
        data = {}
        data['error'] = True
        data['error_msg'] = 'Method not supported'    
        return JsonResponse(data)


@csrf_exempt
def otp_email(request):
    if request.method == "POST":
        email = request.POST['email']
        token = request.POST['token']
        user = Users.objects.filter(email=email).first()
        if user:
            if user.status == 1 and user.is_deleted == 0:
                profile = (Profiles.objects.filter(user_id=user.id))
                if profile:
                    email_verifications(email, token)
                    data = {}
                    data['error'] = False
                    data['status'] = 'complete'
                    data['success_msg'] = 'Verification Code Sent to your Email!'
                    return JsonResponse(data)
                else:
                    email_verifications(email, token)
                    data = {}
                    data['error'] = False
                    data['status'] = 'registered'
                    data['success_msg'] = 'Verification Code Sent to your Email!'
                    return JsonResponse(data)
            else:
                data = {}
                data['error'] = True
                data['error_msg'] = 'User enable to login'
                return JsonResponse(data)
        else:
            email_verifications(email, token)
            data = {}
            data['error'] = False
            data['status'] = 'not registered'
            data['success_msg'] = 'Verification Code Sent to your Email!'
            return JsonResponse(data)
    else:
        data = {}
        data['error'] = True
        data['error_msg'] = 'Method not supported'    
        return JsonResponse(data)

#------------- User Signup --------------     
@csrf_exempt
def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        gender = request.POST['gender']
        dob = request.POST['dob']
        phone = request.POST['phone']
        email = request.POST['email'].lower()
        existed_user = list(Users.objects.filter(phone=phone).values())
        check_fuser = Users.objects.filter(email=email,facebook_key = 1).values()
        check_guser = Users.objects.filter(email=email,google_key = 1).values()
        if not check_guser:
            if not check_fuser:
                if len(existed_user) > 0:
                    existed_user = existed_user[0]
                    if existed_user['status']:
                        if not existed_user['is_deleted']:
                            status = 'registered'
                            success_msg = 'Please complete your profile!'
                            profile = list(Profiles.objects.filter(user_id=existed_user['id']).values())
                            if len(profile) > 0:
                                status = 'completed'
                                success_msg = 'LoggedIn Successfully!'
                                existed_user['profile'] = profile[0]
                                photo = []
                                user_profile_img = list(Profiles.objects.filter(user_id=existed_user['id']).values('id','image'))[0]
                                photo.append(user_profile_img)
                                images = list(Photos.objects.filter(user_id=existed_user['id']).values('id','image'))
                                if images:
                                    for i in [0,1,2,3]:
                                        if i < len(images):
                                            photo.append(images[i])
                                        else:
                                            photo.append({})
                                else:
                                    for i in [0,1,2,3]:
                                        photo.append({})
                                existed_user['images'] = photo
                                
                            else:
                                status = 'registered'
                            return JsonResponse({'error': False, 'status':status,'success_msg': success_msg , 'user': existed_user})
                        else:
                            return JsonResponse({'error': True, 'error_msg': 'User not found!'})
                    else:
                        return JsonResponse({'error': True, 'error_msg': 'User Blocked! Please contact with support to continue!'})
                else:            
                    user = Users(name=name, email=email,phone=phone, dob=dob, gender=gender,status=1)
                    user.save()
                    auto_msg = Auto_msg.objects.filter(id=1).first()
                    message = auto_msg.welcome
                    sbj = 'Welcome'
                    title = 'Welcome to the Serious Dating'
                    auto_message(sbj,email,title,message)
                    user = list(Users.objects.filter(id=user.id).values())[0]
                    return JsonResponse({'error': False,'status':'registered' ,'success_msg': 'Registered Successfully!', 'user': user})
            else:
                return JsonResponse({'error': True, 'error_msg': 'Try to login from facebook'})
        else:
            return JsonResponse({'error': True, 'error_msg': 'Try to login from google'})

    else:
        return JsonResponse({'error': True, 'error_msg': 'Method not supported!'})

#------------- Update Profile --------------
@csrf_exempt
def update_profile(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        profession = request.POST.get('profession')
        marital_status = request.POST.get('marital_status')
        country = request.POST.get('country')
        education = request.POST.get('education')
        image = request.POST.get('image')
        user = Users.objects.filter(id=user_id).first()
        if user:
            profileExists = Profiles.objects.filter(user_id=user_id).first()
            if not profileExists:
                profile = Profiles()
            else:
                profile = profileExists
            if image:
                profile.image = base64_to_image(image)
            else:
                if user.gender == 'Male':
                    image_base = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4ST4RXhpZgAATU0AKgAAAAgABgALAAIAAAAmAAAIYgESAAMAAAABAAEAAAExAAIAAAAmAAAIiAEyAAIAAAAUAAAIrodpAAQAAAABAAAIwuocAAcAAAgMAAAAVgAAEUYc6gAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFdpbmRvd3MgUGhvdG8gRWRpdG9yIDEwLjAuMTAwMTEuMTYzODQAV2luZG93cyBQaG90byBFZGl0b3IgMTAuMC4xMDAxMS4xNjM4NAAyMDIxOjEwOjI3IDE4OjE4OjMxAAAGkAMAAgAAABQAABEckAQAAgAAABQAABEwkpEAAgAAAAM4MwAAkpIAAgAAAAM4MwAAoAEAAwAAAAEAAQAA6hwABwAACAwAAAkQAAAAABzqAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMjAyMToxMDoyNyAxODowOTowMAAyMDIxOjEwOjI3IDE4OjA5OjAwAAAAAAYBAwADAAAAAQAGAAABGgAFAAAAAQAAEZQBGwAFAAAAAQAAEZwBKAADAAAAAQACAAACAQAEAAAAAQAAEaQCAgAEAAAAAQAAE0wAAAAAAAAAYAAAAAEAAABgAAAAAf/Y/9sAQwAIBgYHBgUIBwcHCQkICgwUDQwLCwwZEhMPFB0aHx4dGhwcICQuJyAiLCMcHCg3KSwwMTQ0NB8nOT04MjwuMzQy/9sAQwEJCQkMCwwYDQ0YMiEcITIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIy/8AAEQgBAAEAAwEhAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKC//EALUQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+v/EAB8BAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkKC//EALURAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/aAAwDAQACEQMRAD8A+f6KACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKMU7AGKKLAFFIAooAKKACigAooAKKACigAooAKKA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opAFFABRQAU5DtdT6GnHRgegaRqCWMkOqRZ8pl2Tovp2NN1X4jzPuj0+ARjoJH5P5V9NiMUsPTXL11Pm5ZWsViOeey38zir3Ubq/mMt1O8rnuxqpXzlSo5y5mfQ06cacVGKskFFZlhRQAUUAFFABRQAUUAFFABRQAUUAFFABRQAUUAFFABRQBq6XqBgzE7fun4IPY+tVL6HyblsfdJyPb2r0as/a4aL6xMIx5aj8yrRXnG4UUAFFABRQAUUAFFABRQAUUAFFABRQAUUAFFABRQAUUAFFADlIAPrV3cLu22n/AFiDj3rqoO6cO5nPuUSCDg0lcrNAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACnpI0bblPNXGTi7oTVx0zmVvMJyTUVKbvK4LRBRUjCigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAopgL2pKGAUUgCigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigD//Z/+Ex6Gh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8APD94cGFja2V0IGJlZ2luPSfvu78nIGlkPSdXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQnPz4NCjx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iPjxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+PHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9InV1aWQ6ZmFmNWJkZDUtYmEzZC0xMWRhLWFkMzEtZDMzZDc1MTgyZjFiIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iPjx4bXA6Q3JlYXRvclRvb2w+V2luZG93cyBQaG90byBFZGl0b3IgMTAuMC4xMDAxMS4xNjM4NDwveG1wOkNyZWF0b3JUb29sPjx4bXA6Q3JlYXRlRGF0ZT4yMDIxLTEwLTI3VDE4OjA5OjAwLjgyOTwveG1wOkNyZWF0ZURhdGU+PC9yZGY6RGVzY3JpcHRpb24+PC9yZGY6UkRGPjwveDp4bXBtZXRhPg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPD94cGFja2V0IGVuZD0ndyc/Pv/bAEMAAwICAwICAwMDAwQDAwQFCAUFBAQFCgcHBggMCgwMCwoLCw0OEhANDhEOCwsQFhARExQVFRUMDxcYFhQYEhQVFP/bAEMBAwQEBQQFCQUFCRQNCw0UFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFP/AABEIBDcENwMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/APyqooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooopgFFFFOwBRRRRawBRRRg07XAKKNpo2mjlAKKNpo5pcoBRRRg0coBRRRRYAooopAFFFFIAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooopoAooopgFFKtOoAZRTqXafSgQylWnbT6U5Uz7VoohcZRUnl0bdtPlYiOipVXdSmPkVaptgRbT6UlWDHxSeXVqkxORBRVjyT6H8qTy8dRVeyYuYgoqfy6Qx8ip9mw5iLafSkqwY+KY0fSl7NjuRUU/btpdp9KzcGMiakqVlPpTKnlY7jaKdRUtWAbRTqRqkYlFFFFgCiiikAUUUUgCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiimgCiilWqASlWnUlNCCinqu72p6x1p7MTZFtPpS7M9amWL2qTyM4rojRcieexXKdKfsq0LbjOKlWzLYO39K66eDk7WRlKqkUVjPpUnknA4NaKWJbHGPwqx/ZbtGMKT+FelSy2pPVIydaPUy1gLEcGnG13cYrbh0WVhnYw/A1ch8OyyZ+Rj9Aa9SnktWX2TmnjIR3ZzH2PDAYqX7IVA+X9K7O38H3MjDEDsf901r2fwt1nVGHkWEr4/uqf8K9OHD9Zr4TgqZph4fFNL1POPsp/u/pSfYznofyr22x/Z98UXStnS5V543IR/StOH9mXxR1+yKP8AerqXDVXex5s+I8vpuzrR+88CNixGQpx9KFsT/d4+lfQX/DMPihiM28Y/Gnf8Mv8AibtBHx71t/q3VtsZf60Zd/z+j9589tYsvRTj6U0WWVJ2/pX0L/wzF4nbj7MmPrUNx+zJ4mVfltBx/dyah8M1d0gXE+XP/l9H7z59azbupA+lNazPHyn8q9vvv2ffE9nGN2mysD/dQ/4VzN/8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V0KsFZT1VhnNcd4u+FPh/wAXQsLiyjjlIOJIlw2T614GKyWlW1jofquV+IUoNQxsfmj84p7Ar94MD9KpXFvtPCnNfUnxA/Zc1HT45p9LIvLcchBncPwFeFa34Xn0iYw3Ns8EqnDB1INfCY7IatO7UdD9ky3PsHmEFOhO5xLRVGy7a2bqxaNiCpB9xVCS39K+NxGDdPRn0kKikUm7U2p5IcVEy7a8qVNo6U7jGpKdSNWDVtBiUUUVIBRRRSAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKVaaATBpVpx7Uq1oo9QEp0a5pVXdViOHOCa6adNz2M3Kw1I6tQwhvvD6VLDbZxxWxYaPJdSKqqe3bk19Hg8BOs0lE4q1eMFq7FC301pHC7Wz16V1Xh3wTe6zdRxWts0zE44UmvWvhb+z/f+JEjuLqL7Pa5UlnGCRz0r6d8I/DjRvCNskdraxvIo5kZfm+tfpWX5DCnaVU/Lc+4zw+X3p0nzS7HiPw7/AGaCyxXWrqIU4PlD7x+or33QvBuk+H7eOOxtIotv8RXk1srt28cUV9hTpwpq1NH4PmXEGOzKd6s7LsHHb+VFFFbK582/UKKKKozCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKBrcU8ry2PYjINcf41+Fuh+Mrd1u7SOObB2yRrhiff8q6/FFZyipKz2PQwuMxGEkp0JtNHxf8S/2dNW8LyS3FnGb2z5wyKWwPfHSvF77R3tmlWWPymXtX6byQpNGyyIsikY8thwa8i+JH7PmleKxLc6fElpetklOinkdK+ZxmTUa6cobn7RkPHl+Wjj9+6/U+CprUr2P5VVaEZ5r1rx58JdX8IzOt1ZyBQT+82Eo3I7153c6Y6rkjmvzbHZROi3poft2Ex9LFQU6UrpmFNGF281Ey/jV+e1IPNVpI9uMDNfI1qDi9D14y5loVzTalYH0qNgfSuFpo0QlFFFQxhRRRSAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiilWmgEwaVace1KoPpWijcAC81Jt3YpVjyBkVYjt9zAV30aEpNGUpWEt7fdnNaVtY+aR1IqWzsA7AY616z8N/gzf8Aja6TyopFtlILylCFwc9/wr7XLMoqVnseBj8yo4Om6lV2SOM8N+DrrXryKCyt2mcnGFBOa+pvhP8As72ujQRX+tx+dN8pEOeh5zkflXo3gH4XaP4HtFSC3jkusDfMefUcfnXae9fqWDy+lhkrLU/nviDjatjJOhg9Id+rGQWsNlCkMEaxxr0VRgU+iivUVz8pnUlJ803qwooorQzCiiigQUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABSjr6UlFS/Id7Mo614fsdespba+to7iKQYO4ZP4Gvmj4ufs2SafDNqGgEzW/zM0IzvTp0HevqWkZQy7WAIbqT0H4Vx1sNCvG00fV5PxDjcomnTlePY/MbVNHuLO6aGaBo5F6jaaxbq32noRX378VPgPpnjaKS6s0S01AZY7VwsmccfXj9a+PvHXw7v/CGpTQXds8ZU/eYHDY5r87zXIeW84LQ/pLIuJ8LnEFyvll1R5rKu09KhetS4tPLOG6etVZodtfnGIw7hKzPvY1LlKkapXUg9KZXlyjY3QyilakrJjCiiikAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFNAFFFFMApVoWnjqatRAB1NTQxlj0pixlmHFaFrbk4+U/lXo4ek5tGUpcquJHb5wMH8q19P0szOiIpMjEADGasaNpEl9MIkj3OxAC45/Kvp74K/AbzJI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bHU7mBhgxsRj8a/TkqJPkb7rDafxr8/vjz4dOgePtSjCMiO5ZNy9QecivkM+o+1oqfY/c/DfG+9Uw0uup5DPxIaqP1q9cqS54qnJX4jiIrmZ/RMdtSJqSnUjV5rNhKKKKgAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigApVoWnHtWkRMfH1qwmdwqvH1q3F056134eNzORsaPCZJhwfmIFfoH8C9HGk/D2wBBVphnpjtXwn4PtDearZw43FnXgDPev0Y8KWP8AZnh7TrXGPLhXI/Cv23hyjyUefufhHiNiuXD06PdmrRR/DRX2Z/PAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUhXewGcYpaKl7DR89ftjaTHdeFNPuSpLxyMN2OOgr4euGDNxyK/R/wDaA8MHxN8NdRjRS00K+YoUZOB1r847yLy5mHfOMfSvx3jKm414z7o/qvw5xSr5V7O+sWV6RqWkavzRn6uJRRRUMAooopAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRTAKKKKYBRRRTAKUUlKtIB6ttbPSui8I6s+k63aXUbbWjkVhg+9c76Vf0ogXSeu4fzr1suqcmIgl3OXEQU6Uoy2aP0+8E6sdc8K6bfscmWFSfqK3K4z4OSCT4c6QQMAJ/Suzr+k6OsIvyP4bzSmqeNqwjsmwoooroPKCiiigAooooAKKKKACiiigAooooAKKKKACiiigAoopVpDDHevk39r7w6YdYsb+Mf62PaWxxuGOPrzX1nnrXhv7Vuj/bPA8N4qlmt5jnA6Agf4V5OY0/aYeaPvOC8VLDZvT89D4bvFxJgDHrWfNWnfEtICfxrPuK/A8bFRm0f15T2RXbtTGp1NavEsdCEooorNlBRRRSAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiimgFWnHtTVp3pVrcCRO1XbZfmGeKqR1egy3QZr1sIrnNU2PU/glpo1Hxtp6Y48xT096/QCJ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RTxVKNak7xkroZRRRXKdAUUUUAFFFFQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRTQBRRRVAFFFFABUkeMHvUdSLx70tx+oq/doX9asWdtJfXMcEa7nkIAUeucV9N/Dr9je71W0gvdevFs0kwwtxy+CM16+X5dicxnahHRHi5pnGDyen7XGT5T5z8P+Hb7xJqMVnYwSTzSELhFLfoBX6H/AAT+HQ+HPga1sZVBvJf3k5UY5PQH6c1P4C+C/hn4dKjWFmsl2MZnlwTx6enWu8bLdTlq/YchyBZb+9qP3mfzpxjxks6isLhVanvfuIOnrRS5xxSV9wfkL11CiiimIKKKKACiiigAooooAKKKKACiiigAooooAKUdvfH86SmudkbNkgqpb8s1E9EaU4800j4N/aakH/C0tW5/j/wrxWds16L8aNSbVPH+rzOc7pWxn615xN941+E51U58RP1P7cyWDp4GlF9kVmpjU9qY1fGM+iQlFFFYsYUUUUgCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAVace1NWnHtWkdwFj+8Kv27DI+tUF6Vct8c16WGlZoxnsem/B+8jtPG2lyORtEqg5OB1r9DoZUmhVo8eWRkEdDX5k+G786fqFvMh5WRfw61+i/w+1Max4R065DBi8QB5zX7dw7W58O49mfz14k4WX7vEHRetJRRX1x+EPcKKKKYgooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACl2g8nrSUVEtropaanhf7U/wxi8VeE31i3twb2zyJGQclSBg/pXwdcRmORkYYKnBr9X76xi1KxuLadPMimRo2X2I61+cfxz8CS+AfHF9ZsAYS5aNlHBB5FflHF2WqyxVNep/SnhxnX1ijLAVXrHb0PN2FMqXbkUxq/KD9tG0UUUwCiiioAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKaAKKKKoApy/dptOX7tCA2/B7BfE2nZ6eev8xX6j6a6NptltGP8ARo/5V+WfhdhHr1izcATLyelfqNocq3Gjae6EFWt48Ed+K/WuB/gqH4J4pR92g/Uv0UUV+qn88dgooopiCiiigAooooAKKKKACiiigAooooAKKKKACiiigAqpq0/2XTLyUH7sL5/IVbrnfiFqA0vwZrFwXVMW7KGY4HI/nWNaXLTbPQwFP2mKpx7tH53fEC6F54p1CQHrIf5muRlOWJrW1q4+1X1zIf4nOPzrImr+fszqc1aTP7hwdP2dGEOyRA1ManU1q+XluekJRRRUMAooopAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRTQBSrSUq1a3ActWofvD6VVHWpYztIrooszeqsbmmyNG24DPIr7f/AGX/ABN/anhI2bNua1IGM/wnJ/pXw3ZTBeSevFfS/wCyPrxt/EF3ZM4AmiOATz3r9a4brpTdO+5+Zca4JYvK6j6x1PrfkMc80Up60lfpaP5Pd9LhRRRVEhRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAxGYhWx1xivl/wDbO8JxyabY6zHE29X2SOF46DFfUNeYftGaANe+GGojbua3HmLx+deHm+HWIwVSHkfacI454HN6M1s3Y/OfvTJDUsy+W5X0OKgbpX82SVmf2de6TEooopAFFFFQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUU0AUUUVQBUir8pPJqOrFrCZpEjBCliOScCqim2khN8quaHh6zlvtZtLeFWZ2lXAAJPX2r9PfCNnLYeFtHt5QRLHaxowbqDjmvCf2fP2ctO0W3sfEmo3MeoyyJ5kKR4ZVb3PrnFfR5xtAHAFft3CuV1cDSdWrvLofzN4h5/RzCtDCUNeS9wbtSUUV9+fiwUUUUwCiiigAooooAKKKKACiiigAooooAKKKKACiiikNK7sFeK/tV+Jl0TwCliH2y3smAoODgY/xr2rb8pPf0r5K/bM1wXGtaVp+cfZ4wSAfpXiZtW9jhZNH3vBeDWMzelzbR1+4+X7pvmcdfmNZ8hq1cbQRg5yDmqc33q/A8VJyldn9fQVlYjpGpaRq8hm4lFFFQwCiiikAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABSrSUq1QDqeD0qOnjtW8XZogvWzDcOa9c+A2tDR/H2nSl9iMwVjn1rx+H7wrqPC98+nahb3KHmORf5191kNf2deLPCzXD/AFjD1KXdNH6aRyCRVcNlGAI/GnVg+BtUbWPC2nXTfeaJRW9X7ZHVXP4pxdL2NadPs2gooorQ4gooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigArB8d2H9qeD9YtSM77Zz+QreqG8txdWV1D/AH4XAHUnisK8VKnKL6o78BU9liqc+zR+VevWps9UuYT/AAuf51mtXW/EqxNh4w1KFlKFZTwRXJv/AFr+Y8bD2eJnHzP7qwtT2tCnPukNoooriOoKKKKgAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiimgCiiiqAKKKKACpYflbOOnpxiosGtLQ9Jutb1CGzs4WnuJWCKignJP0q4QlUkow3JlKME5S2R9U/sb+PL6+1C60O5maWHyspuOQuCf8a+szjp3614F+zf8CL/AOHHnapqrKt3cR7VQH5k9cj15Fe+FcKSO+f5V/RGQ08RSwUI4n4j+P8AjbEYPFZrOeCacerXcKKKK+kPz4KKKKYBRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRSr1qX3KWmojHYNx4Vepz+Nfnv8fvEbeIPiFqchYuschRc+3Ffd/jTVk0XwxqN7I4iEULFWY4GcYr81vFGoHU9au7hm3GSRm/OviOJa/s6Ch3P3Tw1wXNOripLbQwp/vmqrVZkPWqzV+LVpXkz+iIrTUY1JStSVwSNQoooqQCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigBVp+aYtP8AStIiJYm2ECtrT7gqw7DIP5ViKRkc1oWzBWU56EV7+X1JQmjkrR5lY/RL4E6wmrfDnT2DKWjXY6qQcYx1r0P9a+Uf2R/GVw17NpLyjy2BKoxx2NfV2flA24xxX7/ga3t6EZo/jzivL3l+aVYvZu/3hRRRXoHxYUUUUwCiiigAooooAKKKKACi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5snJPevzXiTNP+Yemz+keAOHnhKbzDER1lt/mQ3E27naF9s1Vc098butMavyerNyd2z9tirKw2kahulJXG3csKKKKkAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKaAVakyKipVq46sTJFbawq1FNggg1TWpY2G7rXZQm46Ih2e53HgfxVP4b1q2voJGR4yCSD2zX6CfDnxxbeOvDdvfQsC+wCRc5IPrX5owyDcOf1r3v9m34qDwp4gisLuT/AEK4dUZS3bkD+dfqfD2bcrVCoz8r414fWZYR16a/eR/I+3B60UkM4nhR15RvmU+1LX6Yj+WpxcJOMt0FFFFaGIUUUjfeWgYtFFFAgooooAKUUxuop1Sw1DOCB0okby/nPAHWhm2IXyAB1Jryr4t/GSy8HafNFBIslyQR94HGMf41EpRhHnm7JHrZfl1fMq0adFXbKvxa+LUPh+RrS3k+dc7yp+lfMPxE+MFxr1u9q07MrcYrkfF3xGu/EF/NPK/EhOOfeuKuLgzNuJ75r89zniqMYSw2G1Xc/qHIeE6GXwhKrH3l+ZHccyFvXmq7U9m3Uxq/GKknOTbP0tbCUUUVkMKKKKACiiigAooooAKKKKACiiigAooooAKKKKaAKcKbUi0w2HR989K+zP2J9Jkg0HWrx1YByArEcd6+Nrdd0i9+fyr9Av2evFnhW38BadplhfW63qgGaKSVVd3PoCcnpX3vCNJfXPaSdrI/NePqlVZTKjSi3zPoeyY25ptAor9xj3P5JknF2e4UUUVZAUUUUAFFFFABRSNTaAHNTaKKACiilWgB1FFFABRRRQAUUUUAFFFFABRRS8KvI6mpk7K40J2J7DvXC/F74lWvw18M3Vw0q/2jIhSCHIzng5I/Kur13XLXw7pNxqN66pb243NvYAFuwzX5+/GT4l3fxD8TXV1JKwtA5ESE9BxXzmb5gsHRa6s/SuD+G5ZxiVWrfw4PU43xJr1x4i1S4vbxy8spJJZsnrmufmbJqa4k+bgbe3WqzNk4r8MxWIdWbbP6vpU4UoKMNF0RHTWp7UxuleTJm6EooorMoKKKKQBRRRQA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LSjSpRskK0hY+1Rs2abuzSV4cqjlrc9BKwUjUNSVzN3KCiiipAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKcKbTgppoC1YxiSZQ33c5NdHf666xrCj4hjHyqDWLbbbeElsBm6A9apXFwXbrgV9DRrrA0vd+JnJKmqstR9xdGSTg1XZiepphorxp1p1Jc0mdKikrIkU0MaYtDVk2MG6UlFFRcYUUUUAFFFFIAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooopgKtSrnHTI+tRLWt4e0t9Y1OC1QFi7qCFGeO5rooU3WqRpx6siclCLlLobDeDb6x8PWutMoa0nZlDKc7CMdT2619Efst/GYWci+HdXmJjY4hZ24Xg5/pWPH4Rh0JU0SZzPo2pwAW8jfdjmx19iCQK8Zu7C/8AAniaWNiUubWTAb1A5yPzr9UpYWtktWFeGz0Z8PjaeH4gw1TCVdX9k/TIMMKB1xmn9q8r+A/xQTxx4bt4JXDX8ICuCw3MOT0/D9a9TzkDn8K/TqNRVYKcT+TsywFTLcTLDVFsFFFFdB5AUUUh6he56CkVFXdhdwHWgyJkAYBPr1rK8QeLNJ8LWrT6pdxWiKCfndQxx6AnNfO/xG/a7tbdZrTw9GZWOR9oYc9R/wDXrycVmGHwibqyPqMr4dzHNZr2FJ27vY+hfEnjDSPCVnJc6rfx2sSqSY2cB2x2APNfInxg/aj1DxM9xp2iMbLTAWXKthpBx1/z3rxrxV481jxVcvNqN7JNuOQjMSFrmJ5NxB+XcfTivzXNuJJ11yUdEf0Fw7wNhcstWxK9pP8ABFq6vZbiQvK5d26kmqUk26mSSHHHFRlia+Bq4iU2fqSilsrIVnNNLetJSNXFKV9DRA1JRRWYwoooqACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAqW3UM4BO3vyaioqouzuBYupPMfGc4qBqOaSnKTk9RIKKKKgYUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABXUfD+8Njr0E6f62Ng6enHJFcvWn4dujZ6pBJnjdivVy2oqWLpzfcwrw9pTlHufWlqsHinR3twwVbkG5tGB5jlA+aP+XFcV8QvDMnjDw0L9YiNa08bLpFX5mUdHI69qZ8LteM0k2lyStDMr/aLRu+4A8fQ8flXp8ksfn/2zHEuyYeVeW5HGf4uPfrX9KUsPSzfCcz6r8T8gqVauVYl+Wx4j8GfG1x4J8VWl0CwR3CunseM196WFyt5ZwzxYMUiB1x05Ga+DPiT4V/4RPxB9rtMf2fcnzIpF5A77c+or6Y+C/xU0uX4ewPqmoQ20lm3lsZWGeny9/Y14eXzeFcsLVdmj5zjTLf7Ro08wwsbt6Ox7KzKqgnAHvSSMAAR+deLeOP2oPDHh60caZP/AGld9F2J8i49+/8A9avnbxv+074p8RSSiC4+wwvxsi44+tXi85wmE0k7s+OyvgXMsxtKceReZ9neJ/iHoHg+1aTU9ShiIBxCJF3tjtgnPevnr4hftfAxzWvh622IQV86T7x+n618uap4hvtWlMl7dSysectJnNZbXHpxXwmM4orVLqloj9hynw/y/A2lX9+XnsdT4p8faz4suHk1C+mlzyFL8VzUlxu6GoDJu6/zqNm9K+Hr46pWfNUep+nUcPToRUKcUkuw95Cx5qNmppb1pK82VTm1udKQp7UlI1JWF7jFakooqRhRRRSAKKKKQBRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABUtu2yRWHUHNRVJHjFVF2aYdDvvD/iKTTdQstQRsMmMkc8CvpDSdQtdVto7lH/0K8XbLuGArY//AF18laRPut5I8bipyK9a+GvjY/ZTp0zLtYbV3twOvIr984RzeK/dVZaS29T4DiDL3Vh7Wnuj0nWNFTWdIvvD1+F8xQWtZifusOxPvxXimlyXOlz6r4cvC0UskbKFc7R5inj9Ca9w1y8a40uK5t+ZrUBZGX+JRwp/nXnXxE0dNYtoPFFipF9akR30S/ez2fFezxHhJaYqlo1ueRk1a16FVe709Tx6+nZZnVwy7XK/N1yMdazZZyxrT8VW/k6k7quEmG8Y9+axnbjg1+EYvETVVwk9j9MpRXImhZGzimUhYmm15E5tnQkOam0UjVk3cYNSUUVDGFFFFIAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigApVpKVaYF3T7gw3A2nG75TWpp+oSaPfqwz8p/SsFTtYH8a1r6QXAiuApClQrYHGa97AYmdOKcN0c1WClo+p7l4J8eQXUiQ3L4glULID0K9DUt2r+G9amSba9g2EnRmH72Nj1/AYrxrQNWe2uBHnZ0OcV67qE//AAmHhdJ7c77qyX5wOSyev6V+35dmizPBctTWaPhMTgfqle8dmeY/ErS5dL1CCIrut+fJbH3kODXDyV7NeWy+J/Dj6UyZu4R5lvMw+YjHzLn2IFePXsLwXDRum10O0gjHIr8h4iwMsNifaR+GX9WPr8vrc9Lke6/q5Xoo5or5G7PVCiiikAUUUUgCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKVaV+1ADaKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiilWgBVrS028EamOUBkbgA9jWbTlbDZrpo1ZUpXRMlcvys9jMQ3LdQa7j4e+Kv7NvRHM+IJBhhngiuC3GdOeXX9adb3DxsrL95SMGvpsuzGeCrxqxehw4jDwxFNwZ6p4itJtB1TzYXwOJoCPukd1z69K5fx5p8WpRxa3aR7Fmz5qAfdYY/x/Suq0nVE8YaA1mw3X8C7o2AySAOlc9G/2XzYJ1PkXIMZV+NjdM/rX3GcUqeMoucdYSX3M8bCSlSklJWaPP2FRtV/VtPk0+8eBxyvQ46j1qi1fj1SnKlJwluj6eL5lcbRRRWJQUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAU+MZYE9MjNMpyeucVUd9QNG+tzZyKyghJB8pIxVbHltxyPWtSeRL7Q4xuBmgbbjuQef6VkK3UHsc16dVcklJbMyjqjofC2tSaTqUcsbYGcHnqO9df4ogivlS6h4gn5BXswrzSFgrfexXb+FtUGoW506UqwkGE3H7pr7TJsfGdJ4Sts9jycZRamqsSjrsP8AammLLsxd24IkAH3l4wR+v51x0ilW5616MiCK4LSr8qkxz/yrjvE2lrpepPHHzE3zof8AZPI/SvIzzAum/bQ2OnCVbrkZjc0U7aetNr449IKKKKQBRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFKtJSrQBPDP5Ofems2WJqOlPaujnco27E2F3Vc066NtOJAxXB6jrVIZ7U5DtY561tRrSpyUo9CZR5lZnozXEGoWMVyn7xj8t0oP5HH5/lVTVtHW80mTd/r4f3iNnO5D2z7YrG8K6hHDcGOdiIpBtYZ49q3WmeOZoG+aMcAjowr9IhUp5jhde2vqeHOMqNT3TgpgVbn1ycdqiJroW8N3l/qTw2UMkrseFRSTWXq2l3OkXTW93C8Ey9VkGCK/OMRhKtBtyjaJ7casJ6X1KJpKOc0Vws1CiiikAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFKtUALTj2prULRtoA5eOe9OPJplLVxeoh8MhjYHvmuttdTgv4rdpJ/IkQhTz1Fcfg1Irbe/PWvVwePng20tV2MalJVdL2Z6pZ+LNO8G6tbXNshu5Vz98YXnGDXGeOtdm8Sa5NqMqgPKQ21BwPaqjXS6lZqrr+/j4Xb/ABAVWkkM1mVYYdDivaxuY1MfSdJ/D0OKjhoUZ+0+13M1qbT/AOGmHqa+LueswooooJCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigApVpKKaAf9Ka1LHRJV2AbSrSUq1IDz2ptD9qRabET28zQsGXhu1XVZZpjtOQ45rMp8MmxgQe9ddGrytKREo3HXEZjlZTULVpai0VxHHLH95uG9ves1ulZV4qM/dKjsJRRRXMUFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRVdAFWn/AMNR09T71cQGGinyUyp8gClWkooAVqFpKVaQEykbCM4qJuOKX9aa1ay95IBKKKKwAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiimgClWkoqgHntTWpy/dNMpsAooorMAooooAdH96lcHPSmrUhPy1stgIqKKKyYBRRRSAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiiqAVaWm0q07gDUlK1JUgFFFFIApyd6bRTTADRRRQ3cAooopAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUU1uAUUUUPcAooopAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQB//Z"
                    profile.image = base64_to_image(image_base)
                else:
                    image_base = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAAD/4S+SRXhpZgAATU0AKgAAAAgACgALAAIAAAAmAAAIkgEOAAIAAAAyAAAIuAESAAMAAAABAAEAAAExAAIAAAAmAAAI6gEyAAIAAAAUAAAJEIdpAAQAAAABAAAJJJybAAEAAABiAAAS1JyeAAEAAAG+AAATNpyfAAEAAABiAAAU9OocAAcAAAgMAAAAhgAAFVYc6gAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFdpbmRvd3MgUGhvdG8gRWRpdG9yIDEwLjAuMTAwMTEuMTYzODQAcHJvZmlsZSBwbGFjZWhvbGRlciwgZGVmYXVsdCBhdmF0YXIsIGdpcmwgdmVjdG9yAABXaW5kb3dzIFBob3RvIEVkaXRvciAxMC4wLjEwMDExLjE2Mzg0ADIwMjE6MTA6MjcgMTg6MTc6MjAAAAeQAwACAAAAFAAAEYqQBAACAAAAFAAAEZ6ShgAHAAABIAAAEbKSkQACAAAAAzg4AACSkgACAAAAAzg4AACgAQADAAAAAQABAADqHAAHAAAIDAAACX4AAAAAHOoAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA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iS5wf7P8pT/FLIq/pnP6VLaKnmGGgrua+Wp0Fj8LJ+H1LUoolHLLApb/AMeOMfkafc698O/A+SsyX9/H0WIieTI9/uqfyqN9jxcXmk6y5KWi/E888VfGTXdcV7bTB/ZVm3B8pszMPd+3/AcfU15wSWJJJJPJJrRKx5iVhKKYwooAKKACigAooAKKACigAooAKKACigAooAKu6fq+paU5fTtQurRickwTMmfrg80AdZY/F7xnZMu7U0ukAxsuIEIP4gA/rWsPjv4pHWy0g/WGT/45U8qJ5UKfjx4pPSx0gf8AbGT/AOOVn33xm8ZXmPKu7azHcW9upz/33uo5UHKjlNU8Ta5rZb+0tWvLlWOTHJKdn4L0H4CsqmUFFMAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooAKKACigAooA//2QD/4TvbaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLwA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pg0KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNC40LjAtRXhpdjIiPg0KCTxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+DQoJCTxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOk1pY3Jvc29mdFBob3RvPSJodHRwOi8vbnMubWljcm9zb2Z0LmNvbS9waG90by8xLjAvIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyI+DQoJCQk8TWljcm9zb2Z0UGhvdG86TGFzdEtleXdvcmRYTVA+DQoJCQkJPHJkZjpCYWc+DQoJCQkJCTxyZGY6bGk+cGxhY2Vob2xkZXI8L3JkZjpsaT4NCgkJCQkJPHJkZjpsaT5wcm9maWxlPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+YXZhdGFyPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+ZGVmYXVsdDwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPmljb248L3JkZjpsaT4NCgkJCQkJPHJkZjpsaT5waWN0dXJlPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+aW1hZ2U8L3JkZjpsaT4NCgkJCQkJPHJkZjpsaT53b21hbjwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPmZlbWFsZTwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPmdpcmw8L3JkZjpsaT4NCgkJCQkJPHJkZjpsaT5zaWxob3VldHRlPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+aGVhZDwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPnBlcnNvbjwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPmlzb2xhdGVkPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+aWxsdXN0cmF0aW9uPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+dmVjdG9yPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+ZmFjZTwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPmFub255bW91czwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPnVzZXI8L3JkZjpsaT4NCgkJCQkJPHJkZjpsaT5wb3J0cmFpdDwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPmZhY2VsZXNzPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+c29jaWFsPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+bm8gcGhvdG88L3JkZjpsaT4NCgkJCQkJPHJkZjpsaT5ubyBwaWM8L3JkZjpsaT4NCgkJCQkJPHJkZjpsaT5tZWRpYTwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPmNpcmNsZTwvcmRmOmxpPg0KCQkJCTwvcmRmOkJhZz4NCgkJCTwvTWljcm9zb2Z0UGhvdG86TGFzdEtleXdvcmRYTVA+DQoJCQk8ZGM6ZGVzY3JpcHRpb24+DQoJCQkJPHJkZjpBbHQ+DQoJCQkJCTxyZGY6bGkgeG1sOmxhbmc9IngtcmVwYWlyIj5wcm9maWxlIHBsYWNlaG9sZGVyLCBkZWZhdWx0IGF2YXRhciwgZ2lybCB2ZWN0b3I8L3JkZjpsaT4NCgkJCQk8L3JkZjpBbHQ+DQoJCQk8L2RjOmRlc2NyaXB0aW9uPg0KCQkJPGRjOnN1YmplY3Q+DQoJCQkJPHJkZjpCYWc+DQoJCQkJCTxyZGY6bGk+cGxhY2Vob2xkZXI8L3JkZjpsaT4NCgkJCQkJPHJkZjpsaT5wcm9maWxlPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+YXZhdGFyPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+ZGVmYXVsdDwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPmljb248L3JkZjpsaT4NCgkJCQkJPHJkZjpsaT5waWN0dXJlPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+aW1hZ2U8L3JkZjpsaT4NCgkJCQkJPHJkZjpsaT53b21hbjwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPmZlbWFsZTwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPmdpcmw8L3JkZjpsaT4NCgkJCQkJPHJkZjpsaT5zaWxob3VldHRlPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+aGVhZDwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPnBlcnNvbjwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPmlzb2xhdGVkPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+aWxsdXN0cmF0aW9uPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+dmVjdG9yPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+ZmFjZTwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPmFub255bW91czwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPnVzZXI8L3JkZjpsaT4NCgkJCQkJPHJkZjpsaT5wb3J0cmFpdDwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPmZhY2VsZXNzPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+c29jaWFsPC9yZGY6bGk+DQoJCQkJCTxyZGY6bGk+bm8gcGhvdG88L3JkZjpsaT4NCgkJCQkJPHJkZjpsaT5ubyBwaWM8L3JkZjpsaT4NCgkJCQkJPHJkZjpsaT5tZWRpYTwvcmRmOmxpPg0KCQkJCQk8cmRmOmxpPmNpcmNsZTwvcmRmOmxpPg0KCQkJCTwvcmRmOkJhZz4NCgkJCTwvZGM6c3ViamVjdD4NCgkJCTxkYzp0aXRsZT4NCgkJCQk8cmRmOkFsdD4NCgkJCQkJPHJkZjpsaSB4bWw6bGFuZz0ieC1yZXBhaXIiPnByb2ZpbGUgcGxhY2Vob2xkZXIsIGRlZmF1bHQgYXZhdGFyLCBnaXJsIHZlY3RvcjwvcmRmOmxpPg0KCQkJCTwvcmRmOkFsdD4NCgkJCTwvZGM6dGl0bGU+DQoJCQk8ZGM6Y3JlYXRvcj4NCgkJCQk8cmRmOlNlcT4NCgkJCQkJPHJkZjpsaT5WZWN0b3JTdG9jay5jb20vMjc4MjY4ODk8L3JkZjpsaT4NCgkJCQk8L3JkZjpTZXE+DQoJCQk8L2RjOmNyZWF0b3I+DQoJCQk8cGhvdG9zaG9wOkhlYWRsaW5lPg0KCQkJCTxyZGY6QWx0Pg0KCQkJCQk8cmRmOmxpPnByb2ZpbGUgcGxhY2Vob2xkZXIsIGRlZmF1bHQgYXZhdGFyLCBnaXJsIHZlY3RvcjwvcmRmOmxpPg0KCQkJCTwvcmRmOkFsdD4NCgkJCTwvcGhvdG9zaG9wOkhlYWRsaW5lPg0KCQk8L3JkZjpEZXNjcmlwdGlvbj4NCgkJPHJkZjpEZXNjcmlwdGlvbiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iPjx4bXA6Q3JlYXRvclRvb2w+V2luZG93cyBQaG90byBFZGl0b3IgMTAuMC4xMDAxMS4xNjM4NDwveG1wOkNyZWF0b3JUb29sPjx4bXA6Q3JlYXRlRGF0ZT4yMDIxLTEwLTI3VDE4OjE2OjU2Ljg4MjwveG1wOkNyZWF0ZURhdGU+PC9yZGY6RGVzY3JpcHRpb24+PC9yZGY6UkRGPg0KPC94OnhtcG1ldGE+DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8P3hwYWNrZXQgZW5kPSd3Jz8+/+0CLFBob3Rvc2hvcCAzLjAAOEJJTQQEAAAAAAH0HAFaAAMbJUccAgUAMHByb2ZpbGUgcGxhY2Vob2xkZXIsIGRlZmF1bHQgYXZhdGFyLCBnaXJsIHZlY3RvchwCGQALcGxhY2Vob2xkZXIcAhkAB3Byb2ZpbGUcAhkABmF2YXRhchwCGQAHZGVmYXVsdBwCGQAEaWNvbhwCGQAHcGljdHVyZRwCGQAFaW1hZ2UcAhkABXdvbWFuHAIZAAZmZW1hbGUcAhkABGdpcmwcAhkACnNpbGhvdWV0dGUcAhkABGhlYWQcAhkABnBlcnNvbhwCGQAIaXNvbGF0ZWQcAhkADGlsbHVzdHJhdGlvbhwCGQAGdmVjdG9yHAIZAARmYWNlHAIZAAlhbm9ueW1vdXMcAhkABHVzZXIcAhkACHBvcnRyYWl0HAIZAAhmYWNlbGVzcxwCGQAGc29jaWFsHAIZAAhubyBwaG90bxwCGQAGbm8gcGljHAIZAAVtZWRpYRwCGQAGY2lyY2xlHAJpADBwcm9maWxlIHBsYWNlaG9sZGVyLCBkZWZhdWx0IGF2YXRhciwgZ2lybCB2ZWN0b3IcAngAMHByb2ZpbGUgcGxhY2Vob2xkZXIsIGRlZmF1bHQgYXZhdGFyLCBnaXJsIHZlY3RvchwCNwAIMjAyMTEwMjccAjwACzE4MTY1NiswMDAwAAA4QklNBCUAAAAAABA+XrcEhD4Fva3Z8rNHLJ9y/+wAEUR1Y2t5AAEABAAAAGAAAP/bAEMAAwICAwICAwMDAwQDAwQFCAUFBAQFCgcHBggMCgwMCwoLCw0OEhANDhEOCwsQFhARExQVFRUMDxcYFhQYEhQVFP/bAEMBAwQEBQQFCQUFCRQNCw0UFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFP/AABEIA94D4gMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/APznooor3SwooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiikdljGXYIPVjigBaK09C8L614omEWi6NqWsSN0XT7OW4J/wC+FNepeHf2Nfjj4oVGsPhd4jEbdJLy2Fov5zMlK6W4ro8aor6p0X/gmV8etWCmfQdH0gH/AJ/9ahBH1Ee812umf8ElPipcgG+8VeEdP9Qs1zOR+UQH61PtI9yeaPc+IaK/QSy/4I/+JnA+2fE3RYj3EGkzyfzda1oP+CPU5H774rRg4/5ZaCcfrPS9pHuLnifnLRX6Qf8ADnobf+Srndn/AKAHGP8AwIqGf/gj1OB+5+K0ZOP+WugnH6T0e0iHPE/OWiv0Evf+CP8A4mQH7H8TdFlPYT6TPH/J2rmdT/4JKfFS2BNj4q8I6h6BprmAn84iP1o9pHuPnifENFfVOtf8Eyvj1pIYwaDo+rgf8+Gt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oAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA8w+KHwI0b4gLLe22zStcIz9riT5Jj6SqOv+8Pm+tfKni7wZrHgXVm0/WLRrabko4+aOZf7yN0YfqO4FffVY/irwnpXjLSZNN1ezS8tX5Abho2/vI3VW9x+teLjMtp4i84aS/Bn3+Q8WYnK7UMRedL8Y+j/AEfysfAatmnBttejfFf4I6p8N5XvbcvqWgM2FvAvzQ56LKB0/wB4cH2PFebg18dVozoycKisz96weNw+PorEYafNF/1Z9n5EldN4D+IOrfDzWBfaZKCj4E9rIT5U6+jD19GHI/SuW6U4GsoylTkpRdmjorUaWKpyo1oqUXumfdPgD4haV8RNGF9pshWRMLcWkhHmwP6N6g9mHB/MV1FfA/hPxbqfgrW4dU0q4MFzHwQeUlXujjup/wDrjmvsf4afEvTfiRov2q1xBewgC6smbLQse49VPZvwPNfa5fmEcUuSek/z/rsfz5xLwvUyeTxGHvKi/vj5Py7P5PW16nxs+Cfhb4+eA7zwr4ssvtFlN+8guYsC4spgMLNCx+64/JhkMCDX4nftGfs6+KP2a/H0vh3xDGLi0mDTaZq8KEQahADjev8AdYZAdDyp9QQT+9tee/HT4G+GP2gvh/e+FPFFsXt5f3trewgfaLGcDCzRE9GHQjowyp4Ne/CfI/I+FjLlPwBor0P47/A3xN+z18Q73wn4mgHnRjzbS+iU+Rf25OFmiJ7HoV6qwKnpz55XcnfVHT5hRRRQMKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAro/h38PNf+K3jTSfCfhiwbUdb1ObyoIQcKO7O7fwooyzMegBrBtLSe/u4LW1gkubqeRYooIULvI7EBVVRySSQAB1Jr9mv2Gf2RLf9m/wQdV1yCKb4ha3Cp1GbhvsEXDLZxt7HBdh95xjoorOcuVESlyo9C/Zi/Zt8P8A7M/w5h8P6VsvdWuds+r6wU2yX1xjr6rGuSETsOTyxNev0Vy/xH+Iek/DHwtc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y+pg1a4j/mjVrQf8FhpwP33wojJx/wAs9ePX8YK/OWil7OPYXJE/R/8A4fDf9Up/8r//ANz1FP8A8FhZyP3PwpjBx/y1144/SCvzloo9nEOSJ+gl7/wWA8TOD9j+GWixHsZ9Wnk/ki1zOp/8Fa/ipcgix8K+EdP9C0NzOR+coH6V8Q0Uezj2HyRPqnWv+Cmvx61YMINe0fSAf+fDRYQR9DJvNed+Iv2yvjj4oV1v/ij4jEbdY7O5Fov5QqleNUVShFdB8q7GnrvinWvFExl1rWdR1iQ8ltQvJbgn/vtjWWirGMIoQeijFLRVFBRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQB//9k="
                    profile.image = base64_to_image(image_base)
            days_in_year = 365.2425 
            age = int((date.today() - user.dob).days / days_in_year)    
            profile.user_id = user_id
            profile.profession =        profession if profession else None
            profile.marital_status =    marital_status if marital_status else None
            profile.country =           country if country else None
            profile.education =         education if education else None
            profile.age = age
            profile.save()
            if not (Filter.objects.filter(user_id=user_id).first()):
                if user.gender == 'Male':
                    filter = Filter(user_id = user_id,age_from=18,age_to=70,country='All',marital_status='All',gender='Female')
                    filter.save()
                else:
                    filter = Filter(user_id = user_id,age_from=18,age_to=70,country='All',marital_status='All',gender='Male')
                    filter.save()
            user = list(Users.objects.filter(id=user_id).values())[0]
            user['profile'] = list(Profiles.objects.filter(user_id=user['id']).values())[0]
            photo = []
            user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('id','image'))[0]
            photo.append(user_profile_img)
            images = list(Photos.objects.filter(user_id=user['id']).values('id','image'))
            if images:
                for i in [0,1,2,3]:
                    if i < len(images):
                        photo.append(images[i])
                    else:
                        photo.append({})
            else:
                for i in [0,1,2,3]:
                    photo.append({})
            user['images'] = photo
            return JsonResponse({'error': False, 'success_msg': 'Updated Successfully!', 'user': user})
        else:
            data = {}
            data['error'] = True
            data['error_msg'] = 'User Not Found!'    
            return JsonResponse(data)
    else:
        data = {}
        data['error'] = True
        data['error_msg'] = 'Method not supported'    
        return JsonResponse(data)


# ------------------ OTP Phone Number ------------
@csrf_exempt
def otp_phone(request):
    if request.method == "POST":
        phone = request.POST['phone']
        print("///////////OTP//////////////")
        print(phone)
        token = request.POST['token']
        if re.findall(r"^\+(?:[0-9]●?){6,14}[0-9]$", phone):
            url = "https://http-api.d7networks.com/send"
            querystring = {
            "username":"pdoa7175",
            "password":"o2ipYhAE",
            "from":"serious_dating",
            "content":"Your six digit verification code is "+token,
            "dlr-method":"POST",
            "dlr-url":"https://4ba60af1.ngrok.io/receive",
            "dlr":"yes",
            "dlr-level":"3",
            "to":phone
            }
            headers = {
            'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = {}
            data['error'] = False
            data['success_msg'] = 'Message sent Successfully'
            return JsonResponse(data)
        else:
            data = {}
            data['error'] = True
            data['error_msg'] = 'Enter a valid phone number'    
            return JsonResponse(data)
    else:
        data = {}
        data['error'] = True
        data['error_msg'] = 'Method not supported'    
        return JsonResponse(data)


# ------------------ phone number verification ------------
@csrf_exempt
def verify_phone_no(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        phone = request.POST['phone']
        code = request.POST['code']
        user = Profiles.objects.filter(user_id=user_id).first()
        if re.findall(r"^\+(?:[0-9]●?){6,14}[0-9]$", phone):
            if user.phone != phone:
                url = "https://http-api.d7networks.com/send"
                querystring = {
                "username":"pdoa7175",
                "password":"o2ipYhAE",
                "from":"serious_dating",
                "content":"Your six digit verification code is "+code,
                "dlr-method":"POST",
                "dlr-url":"https://4ba60af1.ngrok.io/receive",
                "dlr":"yes",
                "dlr-level":"3",
                "to":phone
                }
                headers = {
                'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                data = {}
                data['error'] = False
                data['success_msg'] = 'Message sent Successfully'
                return JsonResponse(data)
            else:
                data = {}
                data['error'] = True
                data['error_msg'] = 'Phone Number Already In Your Use!!'    
                return JsonResponse(data)
        else:
            data = {}
            data['error'] = True
            data['error_msg'] = 'Enter a valid phone number'    
            return JsonResponse(data)
    else:
        data = {}
        data['error'] = True
        data['error_msg'] = 'Method not supported'    
        return JsonResponse(data)

#------------- Facebook Signup & Login --------------
@csrf_exempt
def fb_social_login(request):
    if request.method == 'POST':
        facebook_key = request.POST['facebook_key']
        name = request.POST['name']
        gender = request.POST['gender']
        dob = request.POST['dob']
        email = request.POST['email']
        user = Users.objects.filter(email=email).first()
        if user:
            if user.facebook_key == facebook_key and user.status == True and user.is_deleted == 0:          
                existed_user = list(Users.objects.filter(email=user.email,facebook_key=user.facebook_key,status=user.status,is_deleted=user.is_deleted).values())
                if len(existed_user) > 0:
                    existed_user = existed_user[0]
                    if existed_user['status']:
                        if not existed_user['is_deleted']:
                            status = 'registered'
                            success_msg = 'Registered Successfully!'
                            profile = list(Profiles.objects.filter(user_id=existed_user['id']).values())
                            if len(profile) > 0:
                                status = 'completed'
                                success_msg = 'LoggedIn Successfully!'
                                existed_user['profile'] = profile[0]
                                photo = []
                                user_profile_img = list(Profiles.objects.filter(user_id=existed_user['id']).values('id','image'))[0]
                                photo.append(user_profile_img)
                                images = list(Photos.objects.filter(user_id=existed_user['id']).values('id','image'))
                                if images:
                                    for i in [0,1,2,3]:
                                        if i < len(images):
                                            photo.append(images[i])
                                        else:
                                            photo.append({})
                                else:
                                    for i in [0,1,2,3]:
                                        photo.append({})
                                existed_user['images'] = photo
                            else:
                                status = 'registered'
                            return JsonResponse({'error': False, 'status':status,'success_msg': success_msg , 'user': existed_user})
                        else:
                            return JsonResponse({'error': True, 'error_msg': 'User not found!'})
                    else:
                        return JsonResponse({'error': True, 'error_msg': 'User Blocked! Please contact with support to continue!'})
            else:
                data = {}
                data['error'] = True
                data['error_msg'] = 'User Unable to login'
                data['fields'] = False
                return JsonResponse(data)
        
        else:
            user =  Users(facebook_key=facebook_key,name=name,gender=gender,dob=dob, email=email, status=True)
            user.save()
            auto_msg = Auto_msg.objects.filter(id=1).first()
            message = auto_msg.welcome
            sbj = 'Welcome'
            title = 'Welcome to the Serious Dating'
            auto_message(sbj,email,title,message)
            user = list(Users.objects.filter(email=email).values())[0]
            data = {}
            data['error'] = False
            data['status'] = 'registered'
            data['success_msg'] = 'Successfully Registered!'
            data['fields'] = False
            data['user'] = user
            return JsonResponse(data, safe=False)

#------------- Google Signup & Login --------------
@csrf_exempt
def google_social_login(request):
    if request.method == 'POST':
        google_key = request.POST['google_key']
        name = request.POST['name']
        gender = request.POST['gender']
        dob = request.POST['dob']
        email = request.POST['email']
        user = Users.objects.filter(email=email).first()
        if user:
            if user.google_key == google_key and user.status == True and user.is_deleted == 0:          
                existed_user = list(Users.objects.filter(email=user.email,google_key=user.google_key,status=user.status,is_deleted=user.is_deleted).values())
                if len(existed_user) > 0:
                    existed_user = existed_user[0]
                    if existed_user['status']:
                        if not existed_user['is_deleted']:
                            status = 'registered'
                            success_msg = 'Registered Successfully!'
                            profile = list(Profiles.objects.filter(user_id=existed_user['id']).values())
                            if len(profile) > 0:
                                status = 'completed'
                                success_msg = 'LoggedIn Successfully!'
                                existed_user['profile'] = profile[0]
                                photo = []
                                user_profile_img = list(Profiles.objects.filter(user_id=existed_user['id']).values('id','image'))[0]
                                photo.append(user_profile_img)
                                images = list(Photos.objects.filter(user_id=existed_user['id']).values('id','image'))
                                if images:
                                    for i in [0,1,2,3]:
                                        if i < len(images):
                                            photo.append(images[i])
                                        else:
                                            photo.append({})
                                else:
                                    for i in [0,1,2,3]:
                                        photo.append({})
                                existed_user['images'] = photo
                            else:
                                status = 'registered'
                            return JsonResponse({'error': False, 'status':status,'success_msg': success_msg , 'user': existed_user})
                        else:
                            return JsonResponse({'error': True, 'error_msg': 'User not found!'})
                    else:
                        return JsonResponse({'error': True, 'error_msg': 'User Blocked! Please contact with support to continue!'})
            else:
                data = {}
                data['error'] = True
                data['error_msg'] = 'User Unable to login'
                data['fields'] = False
                return JsonResponse(data)
        else:
            user =  Users(google_key=google_key,name=name,gender=gender,dob=dob, email=email, status=True)
            user.save()
            auto_msg = Auto_msg.objects.filter(id=1).first()
            message = auto_msg.welcome
            sbj = 'Welcome'
            title = 'Welcome to the Serious Dating'
            auto_message(sbj,email,title,message)
            user = list(Users.objects.filter(email=email).values())[0]
            data = {}
            data['error'] = False
            data['status'] = 'registered'
            data['success_msg'] = 'Successfully Registered!'
            data['fields'] = False
            data['user'] = user
            return JsonResponse(data, safe=False)

# ------------------- Change Email OTP Send ---------------------
@csrf_exempt
def change_email_otp_send(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        new_email = request.POST['new_email']
        token = request.POST['token']
        user = Users.objects.filter(id=user_id,status=1,is_deleted=0).first()
        if user:
            if Users.objects.filter(email=new_email).exists():
                if user.email == new_email:
                    data = {}
                    data['error'] = True
                    data['error_msg'] = 'Email already in your use'
                    return JsonResponse(data)
                else:
                    data = {}
                    data['error'] = True
                    data['error_msg'] = 'Email already exists'
                    return JsonResponse(data)
            else:
                email_verifications(new_email, token)
                data = {}
                data['error'] = False
                data['success_msg'] = 'Email sent successfully'
                return JsonResponse(data)
        else:
            data = {}
            data['error'] = True
            data['error_msg'] = 'User not found'
            return JsonResponse(data)
    else:
        data = {}
        data['error'] = True
        data['error_msg'] = 'Method not supported'
        return JsonResponse(data)

# ------------------- Change Email  ---------------------
@csrf_exempt
def update_email(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        new_email = request.POST['new_email']
        user = Users.objects.filter(id=user_id,status=1,is_deleted=0).first()
        if user:
            user.email = new_email
            user.save()
            data = {}
            data['error'] = False
            data['success_msg'] = 'Email changed successfully'
            user = list(Users.objects.filter(id=user_id).values())[0]
            profile = list(Profiles.objects.filter(user_id=user['id']).values())
            user['profile'] = profile[0]
            photo = []
            user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('id','image'))[0]
            photo.append(user_profile_img)
            images = list(Photos.objects.filter(user_id=user['id']).values('id','image'))
            if images:
                for i in [0,1,2,3]:
                    if i < len(images):
                        photo.append(images[i])
                    else:
                        photo.append({})
            else:
                for i in [0,1,2,3]:
                    photo.append({})
            user['images'] = photo
            data['user'] = user
            return JsonResponse(data, safe=False)
        else:
            data = {}
            data['error'] = True
            data['error_msg'] = 'User not found'
            return JsonResponse(data)
    else:
        data = {}
        data['error'] = True
        data['error_msg'] = 'Method not supported'
        return JsonResponse(data)

# ------------------- Change Phone Number---------------------
@csrf_exempt
def update_phone_no(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        new_phone = request.POST['new_phone']
        userProfile = Profiles.objects.filter(user_id=user_id).first()
        if userProfile:
            userProfile.phone = new_phone
            userProfile.save()
            data = {}
            data['error'] = False
            data['success_msg'] = 'Phone Number changed successfully'
            user = list(Users.objects.filter(id=user_id).values())[0]
            profile = list(Profiles.objects.filter(user_id=user['id']).values())
            user['profile'] = profile[0]
            photo = []
            user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('id','image'))[0]
            photo.append(user_profile_img)
            images = list(Photos.objects.filter(user_id=user['id']).values('id','image'))
            if images:
                for i in [0,1,2,3]:
                    if i < len(images):
                        photo.append(images[i])
                    else:
                        photo.append({})
            else:
                for i in [0,1,2,3]:
                    photo.append({})
            user['images'] = photo
            data['user'] = user
            return JsonResponse(data, safe=False)
        else:
            data = {}
            data['error'] = True
            data['error_msg'] = 'User not found'
            return JsonResponse(data)
    else:
        data = {}
        data['error'] = True
        data['error_msg'] = 'Method not supported'
        return JsonResponse(data)


# ------------------- Expo Token For Notifications ---------------------
@csrf_exempt
def expo_token(request):
    print(request.POST)
    if request.method == "POST":
        user_id = request.POST['user_id']
        expo_token = request.POST['expo_token']
        user = Users.objects.filter(id=user_id).first()
        if user:
            if expo_token == None:
                user.expo_token = None
                user.save()
                return JsonResponse({'error': False,'success_msg': 'Succeeded'})

            else:
                user.expo_token = expo_token
                user.save()
                return JsonResponse({'error': False,'success_msg': 'Succeeded'})

        else:
            return JsonResponse({'error': True,'error_msg': 'User not found'})
    else:
        data = {}
        data['error'] = True
        data['error_msg'] = 'Method not supported'
        return JsonResponse(data)

#------------- Edit Profile --------------
@csrf_exempt
def edit_profile(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        master_image = request.POST.get('master_image')
        image_2 = request.POST.get('image_2')
        image_3 = request.POST.get('image_3')
        image_4 = request.POST.get('image_4')
        image_5 = request.POST.get('image_5')
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        education = request.POST.get('education')
        profession = request.POST.get('profession')
        country = request.POST['country']
        height = request.POST['height']
        marital_status = request.POST['marital_status']
        children = request.POST['children']
        drink = request.POST['drink']
        smoke = request.POST['smoke']
        bio = request.POST['bio']
        user = Users.objects.filter(id=user_id).first()
        profile = Profiles.objects.filter(user_id=user_id).first()
        if master_image:
            img = base64_to_image(master_image)
            profile.image = img
            profile.save()
        if image_2:
            img = base64_to_image(image_2)
            photo = Photos(user_id=user_id,image=img)
            photo.save()
        if image_3:
            img = base64_to_image(image_3)
            photo = Photos(user_id=user_id,image=img)
            photo.save()
        if image_4:
            img = base64_to_image(image_4)
            photo = Photos(user_id=user_id,image=img)
            photo.save()
        if image_5:
            img = base64_to_image(image_5)
            photo = Photos(user_id=user_id,image=img)
            photo.save()
        if name:
            user.name = name
            user.save()
        if dob:
            user.dob = dob
            user.save()
            days_in_year = 365.2425 
            age = int((date.today() - datetime.strptime(user.dob,  '%Y-%m-%d').date()).days / days_in_year)
            profile.age = age
            profile.save()
        if gender:
            user.gender = gender
            user.save()
        if education:
            profile.education = education
            profile.save()
        if profession:
            profile.profession = profession
            profile.save()
        if country:
            profile.country = country
            profile.save()
        if height and height != 'null':
            profile.height = height
            profile.save()
        if marital_status:
            profile.marital_status = marital_status
            profile.save()
        if bio and bio != 'null':
            profile.bio = bio
            profile.save()  
        if str(children) == 'true':
            profile.children = 1
            profile.save()
        elif str(children) == 'false':
            profile.children = 0
            profile.save()
        if str(drink) == 'true':
            profile.drink = 1
            profile.save()
        elif str(drink) == 'false':
            profile.drink = 0
            profile.save()
        if str(smoke) == 'true':
            profile.smoke = 1
            profile.save()
        elif str(smoke) == 'false':
            profile.smoke = 0
            profile.save()
        user = list(Users.objects.filter(id=user_id).values())[0]
        profile = list(Profiles.objects.filter(user_id=user['id']).values())
        if len(profile) > 0:
            user['profile'] = profile[0]
            photo = []
            user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('id','image'))[0]
            photo.append(user_profile_img)
            images = list(Photos.objects.filter(user_id=user['id']).values('id','image'))
            if images:
                for i in [0,1,2,3]:
                    if i < len(images):
                        photo.append(images[i])
                    else:
                        photo.append({})
            else:
                for i in [0,1,2,3]:
                    photo.append({})
            user['images'] = photo
        data = {}
        data['error'] = False
        data['success_msg'] = 'Succeeded'
        data['user'] = user
        return(JsonResponse(data,safe=False))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- Swipe photo --------------
@csrf_exempt
def swipe_photo(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        image_id = request.POST['image_id']
        profile_image = Profiles.objects.filter(user_id=user_id).first()
        image = Photos.objects.filter(id=image_id).first()
        if image:
            temp_profile = image.image
            tem_image = profile_image.image
            profile_image.image = temp_profile
            image.image = tem_image
            profile_image.save()
            image.save()
            profile = list(Profiles.objects.filter(user_id=user_id).values())
            if len(profile) > 0:
                user = list(Users.objects.filter(id=user_id).values())[0]
                data={}
                data['error'] = False
                data['success_msg'] = 'Succeeded'
                user['profile'] = profile[0]
                photo = []
                user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('id','image'))[0]
                photo.append(user_profile_img)
                images = list(Photos.objects.filter(user_id=user['id']).values('id','image'))
                if images:
                    for i in [0,1,2,3]:
                        if i < len(images):
                            photo.append(images[i])
                        else:
                            photo.append({})
                else:
                    for i in [0,1,2,3]:
                        photo.append({})
                user['images'] = photo
            data['user'] = user
            return JsonResponse(data, safe=False)
        else:
            return(JsonResponse({'error':True,'error_msg':"Image not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))
    
#------------- Delete photos --------------
@csrf_exempt
def delete_photo(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        image_id = request.POST['image_id']
        image = Photos.objects.filter(id=image_id).first()
        if image:
            image.delete()
            profile = list(Profiles.objects.filter(user_id=user_id).values())
            if len(profile) > 0:
                user = list(Users.objects.filter(id=user_id).values())[0]
                data={}
                data['error'] = False
                data['success_msg'] = 'Image deleted successfully'
                user['profile'] = profile[0]
                photo = []
                user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('id','image'))[0]
                photo.append(user_profile_img)
                images = list(Photos.objects.filter(user_id=user['id']).values('id','image'))
                if images:
                    for i in [0,1,2,3]:
                        if i < len(images):
                            photo.append(images[i])
                        else:
                            photo.append({})
                else:
                    for i in [0,1,2,3]:
                        photo.append({})
                user['images'] = photo
            data['user'] = user
            return JsonResponse(data, safe=False)

        else:
            return(JsonResponse({'error':True,'error_msg':"Image not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- User Location --------------
@csrf_exempt
def location(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        user = Users.objects.filter(id=user_id).first()
        exist_location = Location.objects.filter(user_id=user_id).first()
        if user:
            if exist_location:
                exist_location.latitude=latitude
                exist_location.longitude=longitude
                exist_location.save()
                return(JsonResponse({'error':False,'success_msg':"Succeeded"}))
            else:
                location = Location(latitude=latitude,longitude=longitude,user_id=user_id)
                location.save()
                return(JsonResponse({'error':False,'success_msg':"Succeeded"}))
        else:
            return(JsonResponse({'error':True,'error_msg':"User not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

# ------------------ Users Filter ------------
@csrf_exempt
def filter(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        age_from = request.POST['age_from']
        age_to = request.POST['age_to']
        country = request.POST['country']
        marital_status = request.POST['marital_status']
        gender = request.POST['gender']
        filter = Filter.objects.filter(user_id=user_id).first()
        if filter:
            filter.age_from = age_from
            filter.age_to = age_to
            filter.country = country
            filter.marital_status = marital_status
            filter.gender = gender
            filter.save()
            return(JsonResponse({'error':False,'success_msg': "Filter update successfully"}))
        else:
            return(JsonResponse({'error':True,'error_msg':"User not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))
        
# ------------------ Random Users ------------
@csrf_exempt
def random_users(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        all_my_blocked = Blocked_users.objects.filter(Q(user_id=user_id) | Q(blocked_user_id=user_id)).values()
        all_my_matching = Matchings.objects.filter(Q(user_id=user_id,liked_by_user1=1) | Q(match_id=user_id,liked_by_user2=1)).values()
        all_my_passing = Dislike.objects.filter(Q(user_id=user_id) | Q(dislike_id=user_id)).values()
        all_my_favourite = Favourite.objects.filter(Q(user_id=user_id) | Q(favourite_id=user_id)).values()
        filter = Filter.objects.filter(user_id=user_id).first()
        user_gender = Users.objects.filter(id=user_id).values()
        ids = []
        filter_ids = []
        ids.append(user_id)
        for block in all_my_blocked:
            if(block['user_id'] == int(user_id)):
                ids.append(block['blocked_user_id'])
            elif(block['blocked_user_id'] == int(user_id)):
                ids.append(block['user_id'])
        for match in all_my_matching:
            if(match['user_id'] == int(user_id)):
                ids.append(match['match_id'])
            elif(match['match_id'] == int(user_id)):
                ids.append(match['user_id'])
        for passing in all_my_passing:
            if(passing['user_id'] == int(user_id)):
                ids.append(passing['dislike_id'])
            elif(passing['dislike_id'] == int(user_id)):
                ids.append(passing['user_id'])
        for favourite in all_my_favourite:
            if(favourite['user_id'] == int(user_id)):
                ids.append(favourite['favourite_id'])
            elif(favourite['favourite_id'] == int(user_id)):
                ids.append(favourite['user_id'])
        users_age = Profiles.objects.all()
        if (int(filter.age_from) != 18 and int(filter.age_to) != 70) or (int(filter.age_from) != 18 and int(filter.age_to) == 70) or (int(filter.age_from) == 18 and int(filter.age_to) != 70):
            for age in users_age:
                if (int(age.age) >= int(filter.age_from)) and (int(age.age) <= int(filter.age_to)):
                    filter_ids.append(age.user_id)
        else:
            for age in users_age:
                filter_ids.append(age.user_id)
        users_country = Profiles.objects.filter(user_id__in=filter_ids)
        filter_ids = []
        if filter.country != 'All':
            for country in users_country:
                if country.country == filter.country:
                    filter_ids.append(country.user_id)
        else:
            for country in users_country:
                filter_ids.append(country.user_id)
        users_marital_status = Profiles.objects.filter(user_id__in=filter_ids)
        filter_ids = []
        if filter.marital_status != 'All':
            filter_ids = []
            for marital_status in users_marital_status:
                if marital_status.marital_status == filter.marital_status:
                    filter_ids.append(marital_status.user_id)
        else:
            for marital_status in users_marital_status:
                filter_ids.append(marital_status.user_id)
        users_gender = Users.objects.filter(id__in=filter_ids)
        filter_ids = []
        if filter.gender != 'All':
            filter_ids = []
            for gender in users_gender:
                if gender.gender == filter.gender:
                    filter_ids.append(gender.id)
        else:
            for gender in users_gender:
                filter_ids.append(gender.id)
                
        pro_user=list(Users.objects.exclude(id__in=ids).filter(status=1,is_deleted=0,id__in=filter_ids).values())
        pro_user_count=Users.objects.exclude(id__in=ids).filter(status=1,is_deleted=0,id__in=filter_ids).values().count()
        users = random.sample(pro_user, pro_user_count)
        results = []
        counter = 0
        for user in users:
            results.append(user)
            results[counter]['profile'] = list(Profiles.objects.filter(user_id=user['id']).values())[0]
            photo = []
            user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('image'))[0]
            photo.append(user_profile_img['image'])
            images = list(Photos.objects.filter(user_id=user['id']).values('image'))
            if images:
                for image in images:
                    photo.append(image['image'])
            results[counter]['images'] = photo
            loc_user1 = Location.objects.filter(user_id=user_id).first()
            loc_user2 = Location.objects.filter(user_id=user['id']).first()
            dis = distance(lat_1=loc_user1.latitude,lon_1=loc_user1.longitude,lat_2=loc_user2.latitude,lon_2=loc_user2.longitude)
            dis = round(dis,1)
            results[counter]['distance'] = dis
            counter += 1
        return JsonResponse(results, safe=False)
    
    else:
        data = {}
        data['error'] = True
        data['error_msg'] = 'Method not supported'
        return JsonResponse(data)
    
#------------- Liked Users --------------
@csrf_exempt
def like(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        match_id = request.POST['match_id']
        user = Users.objects.filter(id=user_id).first()
        otheruser = Users.objects.filter(id=match_id).first()
        limit = Accessories.objects.filter(id=1).first()
        match_1 = Matchings.objects.filter(user_id=user_id,match_id=match_id).first()
        match_2 = Matchings.objects.filter(user_id=match_id,match_id=user_id).first()
        visite = Visited_Users.objects.filter(user_id=user_id,visited_user=match_id).first()
        notiType = 'Like'
        if match_1:
            if not user.pro == 1:
                if Likes.objects.filter(user_id=user_id,date=datetime.now().date()).count() < limit.free_user_allowed_swipes:
                    match_1.liked_by_user1 = 1
                    matching_status = 0
                    if not match_1.liked_by_user2 == 0:
                        match_1.status = 1
                        matching_status = 1
                        auto_msg = Auto_msg.objects.filter(id=1).first()
                        email_1 = user.email
                        email_2 = otheruser.email
                        message = auto_msg.matching
                        sbj = 'Match'
                        title = 'Congratulations You Are Matched With Someone'
                        match_mail(sbj,email_1,email_2,title,message)
                        notiType = 'Match'
                        if Groups.objects.filter(match_id=match_1.id).first():
                            group=Groups.objects.filter(match_id=match_1.id).first()
                            group.status = 1
                            group.save()
                            match_1.deleted_by = 0
                    match_1.save()
                    like = Likes(user_id=user_id,date=datetime.now())
                    like.save()
                    likes_left = limit.free_user_allowed_swipes - Likes.objects.filter(user_id=user_id,date=datetime.now().date()).count()
                    if not visite:
                        visited = Visited_Users(user_id=user_id,visited_user_id=match_id)
                        visited.save()
                        # Send Notification
                        sendPushNotification(user_id, match_id, type=notiType)
                        return (JsonResponse({'error':False,'success_msg':"Like successfully",'likes_left': likes_left,'matching_status':matching_status}))
                    # Send Notification
                    sendPushNotification(user_id, match_id, type=notiType)
                    return(JsonResponse({'error':False,'success_msg':"Like successfully",'likes_left': likes_left,'matching_status':matching_status}))
                else:
                    return (JsonResponse({'error':True,'error_msg':"exceeded_free"}))
            else:
                if Likes.objects.filter(user_id=user_id).count() < limit.pro_user_allowed_swipes:
                    match_1.liked_by_user1 = 1
                    matching_status = 0
                    if not match_1.liked_by_user2 == 0:
                        match_1.status = 1
                        matching_status = 1
                        auto_msg = Auto_msg.objects.filter(id=1).first()
                        email_1 = user.email
                        email_2 = otheruser.email
                        message = auto_msg.matching
                        sbj = 'Match'
                        title = 'Congratulations You Are Matched With Someone'
                        match_mail(sbj,email_1,email_2,title,message)                        
                        group=Groups.objects.filter(match_id=match_1.id).first()
                        group.status = 1
                        group.save()
                        match_1.deleted_by = 0
                        notiType = 'Match'
                    match_1.save()
                    like = Likes(user_id=user_id,date=datetime.now())
                    like.save()
                    likes_left = limit.free_user_allowed_swipes - Likes.objects.filter(user_id=user_id,date=datetime.now().date()).count()
                    if not (Groups.objects.filter(match_id=match_1.id).first()):
                        chat_group = Groups(user_first=match_1.user_id,user_second=match_1.match_id,match_id=match_1.pk,status=1)
                        chat_group.save()
                    if not visite:
                        visited = Visited_Users(user_id=user_id,visited_user_id=match_id)
                        visited.save()
                        # Send Notification
                        sendPushNotification(user_id, match_id, type=notiType)
                        return (JsonResponse({'error':False,'success_msg':"Like successfully",'likes_left': likes_left,'matching_status':matching_status}))
                    # Send Notification
                    sendPushNotification(user_id, match_id, type=notiType)
                    return(JsonResponse({'error':False,'success_msg':"Like successfully",'likes_left': likes_left,'matching_status':matching_status}))
                else:
                    return (JsonResponse({'error':True,'error_msg':"exceeded_pro"}))
        elif match_2:
            if not user.pro == 1:
                if Likes.objects.filter(user_id=user_id,date=datetime.now().date()).count() < limit.free_user_allowed_swipes:
                    match_2.liked_by_user2 = 1
                    matching_status = 0
                    if not match_2.liked_by_user1 == 0:
                        match_2.status = 1
                        matching_status = 1
                        auto_msg = Auto_msg.objects.filter(id=1).first()
                        email_1 = user.email
                        email_2 = otheruser.email
                        message = auto_msg.matching
                        sbj = 'Match'
                        title = 'Congratulations You Are Matched With Someone'
                        match_mail(sbj,email_1,email_2,title,message)
                        notiType = 'Match'
                        if Groups.objects.filter(match_id=match_2.id).first():
                            group=Groups.objects.filter(match_id=match_2.id).first()
                            group.status = 1
                            group.save()
                            match_2.deleted_by = 0
                        else:
                            chat_group = Groups(user_first=match_2.user_id,user_second=match_2.match_id,match_id=match_2.pk,status=1)
                            chat_group.save()
                    match_2.save()
                    like = Likes(user_id=user_id,date=datetime.now())
                    like.save()
                    likes_left = limit.free_user_allowed_swipes - Likes.objects.filter(user_id=user_id,date=datetime.now().date()).count()
                    if not visite:
                        visited = Visited_Users(user_id=user_id,visited_user_id=match_id)
                        visited.save()
                        # Send Notification
                        sendPushNotification(user_id, match_id, type=notiType)
                        return (JsonResponse({'error':False,'success_msg':"Like successfully",'likes_left': likes_left,'matching_status':matching_status}))
                    # Send Notification
                    sendPushNotification(user_id, match_id, type=notiType)
                    return(JsonResponse({'error':False,'success_msg':"Like successfully",'likes_left': likes_left,'matching_status':matching_status}))
                else:
                    return (JsonResponse({'error':True,'error_msg':"exceeded_free"}))
            else:
                if Likes.objects.filter(user_id=user_id).count() < limit.pro_user_allowed_swipes:
                    match_2.liked_by_user2 = 1
                    matching_status = 0
                    if not match_2.liked_by_user1 == 0:
                        match_2.status = 1
                        matching_status = 1
                        auto_msg = Auto_msg.objects.filter(id=1).first()
                        email_1 = user.email
                        email_2 = otheruser.email
                        message = auto_msg.matching
                        sbj = 'Match'
                        title = 'Congratulations You Are Matched With Someone'
                        notiType = 'Match'
                        match_mail(sbj,email_1,email_2,title,message)
                        if Groups.objects.filter(match_id=match_2.id).first():
                            group=Groups.objects.filter(match_id=match_2.id).first()
                            group.status = 1
                            group.save()
                            match_2.deleted_by = 0
                        else:
                            chat_group = Groups(user_first=match_2.user_id,user_second=match_2.match_id,match_id=match_2.pk,status=1)
                            chat_group.save()
                    match_2.save()
                    like = Likes(user_id=user_id,date=datetime.now())
                    like.save()
                    likes_left = limit.free_user_allowed_swipes - Likes.objects.filter(user_id=user_id,date=datetime.now().date()).count()
                    if not visite:
                        visited = Visited_Users(user_id=user_id,visited_user_id=match_id)
                        visited.save()
                        # Send Notification
                        sendPushNotification(user_id, match_id, type=notiType)
                        return (JsonResponse({'error':False,'success_msg':"Like successfully",'likes_left': likes_left,'matching_status':matching_status}))
                    # Send Notification
                    sendPushNotification(user_id, match_id, type=notiType)
                    return(JsonResponse({'error':False,'success_msg':"Like successfully",'likes_left': likes_left,'matching_status':matching_status}))
                else:
                    return (JsonResponse({'error':True,'error_msg':"exceeded_pro"}))
        else:
            if not Matchings.objects.filter(Q(user_id=user_id,match_id=match_id) | Q(user_id=match_id,match_id=user_id)).first():
                if not user.pro == 1:
                    if Likes.objects.filter(user_id=user_id,date=datetime.now().date()).count() < limit.free_user_allowed_swipes:
                        matching = Matchings(user_id=user_id,match_id=match_id,liked_by_user1=1)
                        matching.save()
                        like = Likes(user_id=user_id,date=datetime.now())
                        like.save()
                        likes_left = limit.free_user_allowed_swipes - Likes.objects.filter(user_id=user_id,date=datetime.now().date()).count()
                        if not visite:
                            visited = Visited_Users(user_id=user_id,visited_user_id=match_id)
                            visited.save()
                            # Send Notification
                            sendPushNotification(user_id, match_id, type=notiType)
                            return (JsonResponse({'error':False,'success_msg':"Like successfully",'likes_left': likes_left,'matching_status':0}))
                        # Send Notification
                        sendPushNotification(user_id, match_id, type=notiType)
                        return(JsonResponse({'error':False,'success_msg':"Like successfully",'likes_left': likes_left,'matching_status':0}))
                    else:
                        return (JsonResponse({'error':True,'error_msg':"exceeded_free"}))
                else:
                    if Likes.objects.filter(user_id=user_id).count() < limit.pro_user_allowed_swipes:
                        matching = Matchings(user_id=user_id,match_id=match_id,liked_by_user1=1)
                        matching.save()
                        like = Likes(user_id=user_id,date=datetime.now())
                        like.save()
                        likes_left = limit.pro_user_allowed_swipes - Likes.objects.filter(user_id=user_id).count()
                        if not visite:
                            visited = Visited_Users(user_id=user_id,visited_user_id=match_id)
                            visited.save()
                            # Send Notification
                            sendPushNotification(user_id, match_id, type=notiType)
                            return (JsonResponse({'error':False,'success_msg':"Like successfully",'likes_left': likes_left,'matching_status':0}))
                        # Send Notification
                        sendPushNotification(user_id, match_id, type=notiType)
                        return(JsonResponse({'error':False,'success_msg':"Like successfully",'likes_left': likes_left,'matching_status':0}))
                    else:
                        return (JsonResponse({'error':True,'error_msg':"exceeded_pro"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- Matched Users --------------
@csrf_exempt
def match_list(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        matche_1 = list(Matchings.objects.filter(user_id=user_id,status=1).values())
        matche_2 = list(Matchings.objects.filter(match_id=user_id,status=1).values())
        users=[]
        if len(matche_1) > 0:
            for match in matche_1:
                user = list(Users.objects.filter(id=match['match_id']).values())
                user = user[0]
                user['profile'] = list(Profiles.objects.filter(user_id=user['id']).values())[0]
                photo = []
                user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('image'))[0]
                photo.append(user_profile_img['image'])
                images = list(Photos.objects.filter(user_id=user['id']).values('image'))
                if images:
                    for image in images:
                        photo.append(image['image'])
                user['images'] = photo
                loc_user1 = Location.objects.filter(user_id=user_id).first()
                loc_user2 = Location.objects.filter(user_id=user['id']).first()
                dis = distance(lat_1=loc_user1.latitude,lon_1=loc_user1.longitude,lat_2=loc_user2.latitude,lon_2=loc_user2.longitude)
                dis = round(dis,1)
                user['distance'] = dis
                users.append(user)
        if len(matche_2) > 0:
            for match in matche_2:
                user = list(Users.objects.filter(id=match['user_id']).values())
                user = user[0]
                user['profile'] = list(Profiles.objects.filter(user_id=user['id']).values())[0]
                photo = []
                user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('image'))[0]
                photo.append(user_profile_img['image'])
                images = list(Photos.objects.filter(user_id=user['id']).values('image'))
                if images:
                    for image in images:
                        photo.append(image['image'])
                user['images'] = photo
                loc_user1 = Location.objects.filter(user_id=user_id).first()
                loc_user2 = Location.objects.filter(user_id=user['id']).first()
                dis = distance(lat_1=loc_user1.latitude,lon_1=loc_user1.longitude,lat_2=loc_user2.latitude,lon_2=loc_user2.longitude)
                dis = round(dis,1)
                user['distance'] = dis
                users.append(user)
        return(JsonResponse({'error':False,'success_msg':"Succedded!!",'user':users}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))


#------------- UnMatched Users --------------
@csrf_exempt
def unmatch(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        match_id = request.POST['match_id']
        matches_1 = Matchings.objects.filter(user_id=user_id,match_id=match_id,status=1).first()
        matches_2 = Matchings.objects.filter(user_id=match_id,match_id=user_id,status=1).first()
        if matches_1:
            matches_1.liked_by_user1 = 0
            matches_1.deleted_by = user_id
            matches_1.status = 0
            matches_1.save()
            if Groups.objects.filter(match_id=matches_1.id).first():
                group=Groups.objects.filter(match_id=matches_1.id).first()
                group.status = 0
                group.save()
            dislike = Dislike(user_id=user_id,dislike_id=matches_1.match_id)
            dislike.save()
            return(JsonResponse({'error':False,'success_msg':"Succedded!!"}))
        elif matches_2:
            matches_2.liked_by_user2 = 0
            matches_2.deleted_by = user_id
            matches_2.status = 0
            matches_2.save()
            if Groups.objects.filter(match_id=matches_2.id).first():
                group=Groups.objects.filter(match_id=matches_2.id).first()
                group.status = 0
                group.save()
            dislike = Dislike(user_id=user_id,dislike_id=matches_2.user_id)
            dislike.save()
            return(JsonResponse({'error':False,'success_msg':"Succedded!!"}))
        else:
            return(JsonResponse({'error':True,'error_msg':"User Not Found!!"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- Left Likes  --------------
@csrf_exempt
def left_likes(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user = Users.objects.filter(id=user_id).first()
        limit = Accessories.objects.filter(id=1).first()
        profile = Profiles.objects.filter(user_id=user_id).first()
        percentage = 0
        increment = 100/16
        percentage = (percentage + increment) if user.name else percentage
        percentage = (percentage + increment) if user.email else percentage
        percentage = (percentage + increment) if user.gender else percentage
        percentage = (percentage + increment) if user.dob  else percentage
        percentage = (percentage + increment) if user.phone  else percentage
        percentage = (percentage + increment) if profile.image else percentage
        percentage = (percentage + increment) if profile.profession else percentage
        percentage = (percentage + increment) if profile.education else percentage
        percentage = (percentage + increment) if profile.country else percentage
        percentage = (percentage + increment) if profile.marital_status  else percentage
        percentage = (percentage + increment) if profile.height else percentage
        percentage = (percentage + increment) if (profile.smoke == 1 or profile.smoke == 0)  else percentage
        percentage = (percentage + increment) if (profile.drink == 1 or profile.drink == 0)  else percentage
        percentage = (percentage + increment) if (profile.children == 1 or profile.children == 0)  else percentage
        percentage = (percentage + increment) if profile.address else percentage
        percentage = (percentage + increment) if profile.bio else percentage
        if user.pro == 1:
            likes_left = limit.pro_user_allowed_swipes - Likes.objects.filter(user_id=user_id,date=datetime.now().date()).count()
            return(JsonResponse({'error':False,'success_msg':"succeeded",'percentage':int(percentage),'likes_left': likes_left}))
        else:
            likes_left = limit.free_user_allowed_swipes - Likes.objects.filter(user_id=user_id,date=datetime.now().date()).count()
            return(JsonResponse({'error':False,'success_msg':"succeeded",'percentage':int(percentage),'likes_left': likes_left}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))
    

#------------- Liked Users List --------------
@csrf_exempt
def likes_list(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        likes = list(Matchings.objects.filter(Q(user_id=user_id,liked_by_user1=1) | Q(match_id=user_id,liked_by_user2=1)).values())
        users = []
        if len(likes) > 0:
            for like in likes:
                if int(like['user_id'])== int(user_id):
                    user = list(Users.objects.filter(id=like['match_id'],status=1,is_deleted=0).values())
                    if len(user) > 0:
                        user = user[0]
                        user['profile'] = list(Profiles.objects.filter(user_id=user['id']).values())[0]
                        photo = []
                        user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('image'))[0]
                        photo.append(user_profile_img['image'])
                        images = list(Photos.objects.filter(user_id=user['id']).values('image'))
                        if images:
                            for image in images:
                                photo.append(image['image'])
                        user['images'] = photo
                        loc_user1 = Location.objects.filter(user_id=user_id).first()
                        loc_user2 = Location.objects.filter(user_id=user['id']).first()
                        dis = distance(lat_1=loc_user1.latitude,lon_1=loc_user1.longitude,lat_2=loc_user2.latitude,lon_2=loc_user2.longitude)
                        dis = round(dis,1)
                        user['distance'] = dis
                        users.append(user)
                elif int(like['match_id']) == int(user_id):
                    user = list(Users.objects.filter(id=like['user_id'],status=1,is_deleted=0).values())
                    if len(user) > 0:
                        user = user[0]
                        user['profile'] = list(Profiles.objects.filter(user_id=user['id']).values())[0]
                        photo = []
                        user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('image'))[0]
                        photo.append(user_profile_img['image'])
                        images = list(Photos.objects.filter(user_id=user['id']).values('image'))
                        if images:
                            for image in images:
                                photo.append(image['image'])
                        user['images'] = photo
                        sloc_user1 = Location.objects.filter(user_id=user_id).first()
                        loc_user2 = Location.objects.filter(user_id=user['id']).first()
                        dis = distance(lat_1=loc_user1.latitude,lon_1=loc_user1.longitude,lat_2=loc_user2.latitude,lon_2=loc_user2.longitude)
                        dis = round(dis,1)
                        user['distance'] = dis
                        users.append(user)
            return JsonResponse({'error': False, 'success_msg': 'liked users!', 'user': users})
        else:
            return(JsonResponse({'error':False,'success_msg':"liked users", 'user': users}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- Liked by Users List --------------
@csrf_exempt
def liked_by_list(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        likes = list(Matchings.objects.all().values())
        users = []
        if len(likes) > 0:
            for like in likes:
                if int(like['user_id']) == int(user_id) and int(like['liked_by_user2'])== int(1):
                    user = list(Users.objects.filter(id=int(like['match_id']),status=1,is_deleted=0).values())
                    if len(user) > 0:
                        user = user[0]
                        user['profile'] = list(Profiles.objects.filter(user_id=user['id']).values())[0]
                        photo = []
                        user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('image'))[0]
                        photo.append(user_profile_img['image'])
                        images = list(Photos.objects.filter(user_id=user['id']).values('image'))
                        if images:
                            for image in images:
                                photo.append(image['image'])
                        user['images'] = photo
                        passed =  Dislike.objects.filter(user_id=like['user_id'],dislike_id=like['match_id']).first()
                        blocked = Blocked_users.objects.filter(user_id=like['user_id'],blocked_user_id=like['match_id']).first()
                        if passed or blocked:
                           user['matching_status'] = 2
                        else:
                            if int(like['liked_by_user1']) == int(1):
                                user['matching_status'] = 1
                            else:
                                user['matching_status'] = 0
                        loc_user1 = Location.objects.filter(user_id=user_id).first()
                        loc_user2 = Location.objects.filter(user_id=user['id']).first()
                        dis = distance(lat_1=loc_user1.latitude,lon_1=loc_user1.longitude,lat_2=loc_user2.latitude,lon_2=loc_user2.longitude)
                        dis = round(dis,1)
                        user['distance'] = dis
                        users.append(user)
                elif int(like['match_id']) == int(user_id) and int(like['liked_by_user1'])==int(1):
                    user = list(Users.objects.filter(id=int(like['user_id']),status=1,is_deleted=0).values())
                    if len(user) > 0:
                        user = user[0]
                        user['profile'] = list(Profiles.objects.filter(user_id=user['id']).values())[0]
                        photo = []
                        user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('image'))[0]
                        photo.append(user_profile_img['image'])
                        images = list(Photos.objects.filter(user_id=user['id']).values('image'))
                        if images:
                            for image in images:
                                photo.append(image['image'])
                        user['images'] = photo
                        passed =  Dislike.objects.filter(user_id=like['match_id'],dislike_id=like['user_id']).first()
                        blocked = Blocked_users.objects.filter(user_id=like['match_id'],blocked_user_id=like['user_id']).first()
                        if passed or blocked:
                           user['matching_status'] = 2
                        else:
                            if int(like['liked_by_user2']) == int(1):
                                user['matching_status'] = 1
                            else:
                                user['matching_status'] = 0
                        loc_user1 = Location.objects.filter(user_id=user_id).first()
                        loc_user2 = Location.objects.filter(user_id=user['id']).first()
                        dis = distance(lat_1=loc_user1.latitude,lon_1=loc_user1.longitude,lat_2=loc_user2.latitude,lon_2=loc_user2.longitude)
                        dis = round(dis,1)
                        user['distance'] = dis
                        users.append(user)
            return JsonResponse({'error': False, 'success_msg': 'liked users!', 'user': users})
        else:
            return(JsonResponse({'error':False,'success_msg':"liked users", 'user': users}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- unlike User --------------
@csrf_exempt
def unlike(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        unlike_id = request.POST['unlike_id']
        unlike_by_user_1 = Matchings.objects.filter(user_id=user_id,match_id=unlike_id).first()
        unlike_by_user_2 = Matchings.objects.filter(user_id=unlike_id,match_id=user_id).first()
        dislike = Dislike.objects.filter(user_id=user_id,dislike_id=unlike_id).first()
        if unlike_by_user_1:
            unlike_by_user_1.liked_by_user1 = 0
            unlike_by_user_1.status = 0
            if not unlike_by_user_1.deleted_by:
                unlike_by_user_1.deleted_by = user_id
                if Groups.objects.filter(match_id=unlike_by_user_1.id).first():
                    group=Groups.objects.filter(match_id=unlike_by_user_1.id).first()
                    group.status = 0
                    group.save()
            unlike_by_user_1.save()
            return(JsonResponse({'error':False,'success_msg':"Successfully unliked"}))
        elif unlike_by_user_2:
            unlike_by_user_2.liked_by_user2 = 0
            unlike_by_user_2.status = 0
            if not unlike_by_user_2.deleted_by:
                unlike_by_user_2.deleted_by = user_id
                if Groups.objects.filter(match_id=unlike_by_user_2.id).first():
                    group=Groups.objects.filter(match_id=unlike_by_user_2.id).first()
                    group.status = 0
                    group.save()
            unlike_by_user_2.save()
            return(JsonResponse({'error':False,'success_msg':"Successfully unliked"}))
        else:
            return(JsonResponse({'error':False,'success_msg':"unliked users not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- Disiked Users --------------
@csrf_exempt
def dislike(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        dislike_id = request.POST['dislike_id']
        dislike = Dislike.objects.filter(user_id=user_id,dislike_id=dislike_id).first()
        visite = Visited_Users.objects.filter(user_id=user_id,visited_user=dislike_id).first()
        if not dislike:
            disliked = Dislike(user_id=user_id,dislike_id=dislike_id)
            disliked.save()
            if not visite:
                visited = Visited_Users(user_id=user_id,visited_user_id=dislike_id)
                visited.save()
                return (JsonResponse({'error':False,'success_msg':"Successfully pass"}))
            
            return (JsonResponse({'error':False,'success_msg':"Successfully pass"}))
        else:
            return(JsonResponse({'error':True,'error_msg':"Alredy pass"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- Disliked Users List --------------
@csrf_exempt
def dislikes_list(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        dislikes = list(Dislike.objects.filter(user_id=user_id).values())
        users = []
        if len(dislikes) > 0:
            for dislike in dislikes:
                user = list(Users.objects.filter(id=dislike['dislike_id'],status=1,is_deleted=0).values())
                if len(user) > 0:
                    user = user[0]
                    user['profile'] = list(Profiles.objects.filter(user_id=user['id']).values())[0]
                    photo = []
                    user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('image'))[0]
                    photo.append(user_profile_img['image'])
                    images = list(Photos.objects.filter(user_id=user['id']).values('image'))
                    if images:
                        for image in images:
                            photo.append(image['image'])
                    user['images'] = photo
                    loc_user1 = Location.objects.filter(user_id=user_id).first()
                    loc_user2 = Location.objects.filter(user_id=user['id']).first()
                    dis = distance(lat_1=loc_user1.latitude,lon_1=loc_user1.longitude,lat_2=loc_user2.latitude,lon_2=loc_user2.longitude)
                    dis = round(dis,1)
                    user['distance'] = dis
                    users.append(user)
            return JsonResponse({'error': False, 'success_msg': 'disliked users!', 'user': users})
        else:
            return(JsonResponse({'error':False,'success_msg':"disliked users", 'user': users}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- Disiked User --------------
@csrf_exempt
def undislike(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        dislike_id = request.POST['dislike_id']
        dislike = Dislike.objects.filter(user_id=user_id,dislike_id=dislike_id).first()
        if dislike:
            dislike.delete()
            return(JsonResponse({'error':False,'success_msg':"Successfully undislike"}))
        else:
            return(JsonResponse({'error':False,'success_msg':"disliked users not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- Favourite User --------------
@csrf_exempt
def favourite(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        favourite_id = request.POST['favourite_id']
        favourite_user = Users.objects.filter(id=favourite_id).first()
        visite = Visited_Users.objects.filter(user_id=user_id,visited_user=favourite_id).first()
        if favourite_user:
            if not Favourite.objects.filter(user_id=user_id,favourite_id=favourite_id).first():
                favourited = Favourite(user_id=user_id,favourite_id=favourite_id)
                favourited.save()
                if not visite:
                    visited = Visited_Users(user_id=user_id,visited_user_id=favourite_id)
                    visited.save()
                    return(JsonResponse({'error':False,'success_msg':"Successfully user favourite"}))
                return(JsonResponse({'error':False,'success_msg':"Successfully user favourite"}))
            else:
                return(JsonResponse({'error':True,'error_msg':"User already favourite"}))
        else:
            return(JsonResponse({'error':True,'error_msg':"users not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- Favourite Users List --------------
@csrf_exempt
def favourite_list(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        favourites = list(Favourite.objects.filter(user_id=user_id).values())
        users = []
        if len(favourites) > 0:
            for favourite in favourites:
                user = list(Users.objects.filter(id=favourite['favourite_id'],status=1,is_deleted=0).values())
                if len(user) > 0:
                    user = user[0]
                    user['profile'] = list(Profiles.objects.filter(user_id=user['id']).values())[0]
                    photo = []
                    user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('image'))[0]
                    photo.append(user_profile_img['image'])
                    images = list(Photos.objects.filter(user_id=user['id']).values('image'))
                    if images:
                        for image in images:
                            photo.append(image['image'])
                    user['images'] = photo
                    loc_user1 = Location.objects.filter(user_id=user_id).first()
                    loc_user2 = Location.objects.filter(user_id=user['id']).first()
                    dis = distance(lat_1=loc_user1.latitude,lon_1=loc_user1.longitude,lat_2=loc_user2.latitude,lon_2=loc_user2.longitude)
                    dis = round(dis,1)
                    user['distance'] = dis
                    users.append(user)
            return JsonResponse({'error': False, 'success_msg': 'Favourite users!', 'user': users})
        else:
            return(JsonResponse({'error':False,'success_msg':"Favourite users", 'user': users}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- Unfavourite User --------------
@csrf_exempt
def unfavourite(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        favourite_id = request.POST['favourite_id']
        favourited_user = Favourite.objects.filter(user_id=user_id,favourite_id=favourite_id).first()
        if favourited_user:
            favourited_user.delete()
            return(JsonResponse({'error':False,'success_msg':"successfully unfavourite user"}))
        else:
            return(JsonResponse({'error':True,'error_msg':"User not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- Visited Users List --------------
@csrf_exempt
def visited_list(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        visites = list(Visited_Users.objects.filter(visited_user_id=user_id).values())
        users = []
        if len(visites) > 0:
            for visite in visites:
                user = list(Users.objects.filter(id=visite['user_id'],status=1,is_deleted=0).values())
                if len(user) > 0:
                    user = user[0]
                    user['profile'] = list(Profiles.objects.filter(user_id=user['id']).values())[0]
                    photo = []
                    user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('image'))[0]
                    photo.append(user_profile_img['image'])
                    images = list(Photos.objects.filter(user_id=user['id']).values('image'))
                    if images:
                        for image in images:
                            photo.append(image['image'])
                    user['images'] = photo
                    loc_user1 = Location.objects.filter(user_id=user_id).first()
                    loc_user2 = Location.objects.filter(user_id=user['id']).first()
                    dis = distance(lat_1=loc_user1.latitude,lon_1=loc_user1.longitude,lat_2=loc_user2.latitude,lon_2=loc_user2.longitude)
                    dis = round(dis,1)
                    user['distance'] = dis
                    users.append(user)
            return JsonResponse({'error': False, 'success_msg': 'visited users!', 'user': users})
        else:
            return(JsonResponse({'error':False,'success_msg':"visited users", 'user': users}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- Block User --------------
@csrf_exempt
def block(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        blocked_user_id = request.POST['blocked_user_id']
        block_user = Users.objects.filter(id=blocked_user_id).first()
        favourite = Favourite.objects.filter(user_id=user_id,favourite_id=blocked_user_id).first()
        passed = Dislike.objects.filter(user_id=user_id,dislike_id=blocked_user_id).first()
        matche_1 = Matchings.objects.filter(user_id=user_id,match_id=blocked_user_id,status=0).first()
        matche_2 = Matchings.objects.filter(match_id=user_id,user_id=blocked_user_id,status=0).first()      
        if block_user:
            if not Blocked_users.objects.filter(user_id=user_id,blocked_user_id=blocked_user_id).first():
                blocked = Blocked_users(user_id=user_id,blocked_user_id=blocked_user_id)
                blocked.save()
                sbj = 'Someone has blocked you!!'
                email = block_user.email
                auto_msg = Auto_msg.objects.filter(id=1).first()
                message =auto_msg.user_block
                title='Someone Has Blocked You'
                auto_message(sbj,email,title,message)
                if favourite:
                    favourite.delete() 
                if passed:
                    passed.delete()
                if matche_1:
                    matche_1.liked_by_user1 = 0
                    matche_1.save() 
                if matche_2:
                    matche_2.liked_by_user2 = 0
                    matche_2.save()
                return(JsonResponse({'error':False,'success_msg':"Successfully user block"}))
            else:
                return(JsonResponse({'error':True,'error_msg':"User already blocked"}))
        else:
            return(JsonResponse({'error':True,'error_msg':"users not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))


#------------- Block User From Chat --------------
@csrf_exempt
def block_from_chat(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        blocked_user_id = request.POST['blocked_user_id']
        block_user = Users.objects.filter(id=blocked_user_id).first()
        favourite = Favourite.objects.filter(user_id=user_id,favourite_id=blocked_user_id).first()
        passed = Dislike.objects.filter(user_id=user_id,dislike_id=blocked_user_id).first()
        match = Matchings.objects.filter(Q(user_id=user_id,match_id=blocked_user_id) | Q(match_id=user_id,user_id=blocked_user_id)).first()
        group = Groups.objects.filter(Q(user_first=user_id,user_second=blocked_user_id) | Q(user_first=blocked_user_id,user_second=user_id)).first()
        if block_user:
            if not Blocked_users.objects.filter(user_id=user_id,blocked_user_id=blocked_user_id).first():
                blocked = Blocked_users(user_id=user_id,blocked_user_id=blocked_user_id)
                blocked.save()
                sbj = 'Someone has blocked you!!'
                email = block_user.email
                auto_msg = Auto_msg.objects.filter(id=1).first()
                message =auto_msg.user_block
                title='Someone Has Blocked You'
                auto_message(sbj,email,title,message)
                if favourite:
                    favourite.delete() 
                if passed:
                    passed.delete()
                if match:
                    match.liked_by_user1 = 0
                    match.liked_by_user2 = 0
                    match.status = 0
                    match.deleted_by = user_id
                    match.save()
                if group:
                    group.blocked_by_user = blocked_user_id
                    group.unblock_by_user = user_id
                    group.status = 0
                    group.save()
                return(JsonResponse({'error':False,'success_msg':"Successfully user block"}))
            else:
                return(JsonResponse({'error':True,'error_msg':"User already blocked"}))
        else:
            return(JsonResponse({'error':True,'error_msg':"users not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- Blocked Users List --------------
@csrf_exempt
def block_list(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        blocks = list(Blocked_users.objects.filter(user_id=user_id).values())
        users = []
        if len(blocks) > 0:
            for block in blocks:
                user = list(Users.objects.filter(id=block['blocked_user_id'],status=1,is_deleted=0).values())
                if len(user) > 0:
                    user = user[0]
                    user['profile'] = list(Profiles.objects.filter(user_id=user['id']).values())[0]
                    photo = []
                    user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('image'))[0]
                    photo.append(user_profile_img['image'])
                    images = list(Photos.objects.filter(user_id=user['id']).values('image'))
                    if images:
                        for image in images:
                            photo.append(image['image'])
                    user['images'] = photo
                    loc_user1 = Location.objects.filter(user_id=user_id).first()
                    loc_user2 = Location.objects.filter(user_id=user['id']).first()
                    dis = distance(lat_1=loc_user1.latitude,lon_1=loc_user1.longitude,lat_2=loc_user2.latitude,lon_2=loc_user2.longitude)
                    dis = round(dis,1)
                    user['distance'] = dis
                    users.append(user)
            return JsonResponse({'error': False, 'success_msg': 'Blocked users!', 'user': users})
        else:
            return(JsonResponse({'error':False,'success_msg':"Blocked users", 'user': users}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))

#------------- Unblock User --------------
@csrf_exempt
def unblock(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        blocked_user_id = request.POST['blocked_user_id']
        blocked_user = Blocked_users.objects.filter(user_id=user_id,blocked_user_id=blocked_user_id).first()
        group = Groups.objects.filter(Q(user_first=user_id,user_second=blocked_user_id) | Q(user_first=blocked_user_id,user_second=user_id)).first()
        if blocked_user:
            blocked_user.delete()
            if group:
                if group.blocked_by_user == int(blocked_user_id):
                    group.blocked_by_user = None
                    group.unblock_by_user = None
                    group.save()
            return(JsonResponse({'error':False,'success_msg':"successfully unblock_user"}))
        else:
            return(JsonResponse({'error':True,'error_msg':"User not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))
    
#------------- Packages --------------       
@csrf_exempt
def packages(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        subscription = Purchased_subscriptions.objects.filter(user_id=user_id,is_valid=1).first()
        pro_likes = list(Accessories.objects.all().values('pro_user_allowed_swipes'))
        likes = pro_likes[0]['pro_user_allowed_swipes']
        packages = list(Packages.objects.filter(status=1).values())
        if subscription:
            purchased_packgae = list(Packages.objects.filter(id=subscription.package_id).values())
            return(JsonResponse({'error':False,'success_msg':"Succeeded",'likes_allowed':likes,'purchase':True,'purchased_packgae':purchased_packgae,'packages':packages}))
        return(JsonResponse({'error':False,'success_msg':"Succeeded",'likes_allowed':likes,'purchase':False,'packages':packages}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))
    
    
#------------- Purchased Subscription --------------       
@csrf_exempt
def subscription(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        package_id = request.POST['package_id']
        token = request.POST['token']
        user = Users.objects.filter(id=user_id).first()
        package = Packages.objects.filter(id=package_id).first()
        subscription = Purchased_subscriptions.objects.filter(user_id=user_id,is_valid=True).first()
        if user:
            if subscription:
                if subscription.is_valid:
                    subscription.is_valid = False
                    user.pro = False
                    subscription.save()
                    user.save()
            amount = package.amount
            charge = chargeStripe(token,amount)
            if not charge['error']:
                amount = package.amount
                duration = package.duration_in_days
                transection_id = charge['charge'].id
                from_date = datetime.now()
                to_date = from_date + timedelta(duration)
                user.pro = True
                subscription = Purchased_subscriptions(user_id=user_id,package_id=package_id,transection_id=transection_id,amount=amount,from_date=from_date,to_date=to_date,is_valid=True)
                user.save()
                subscription.save()
                user = list(Users.objects.filter(id=user_id).values())[0]
                profile = list(Profiles.objects.filter(user_id=user['id']).values())
                if len(profile) > 0:
                    user['profile'] = profile[0]
                    photo = []
                    user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('id','image'))[0]
                    photo.append(user_profile_img)
                    images = list(Photos.objects.filter(user_id=user['id']).values('id','image'))
                    if images:
                        for i in [0,1,2,3]:
                            if i < len(images):
                                photo.append(images[i])
                            else:
                                photo.append({})
                    else:
                        for i in [0,1,2,3]:
                            photo.append({})
                    user['images'] = photo
                return(JsonResponse({'error':False,'success_msg':"Package Subscribed Successfully",'user':user}))
            else:
                return(JsonResponse({'error':True,'error_msg':charge['error_msg']}))
        else:
            return(JsonResponse({'error':True,'error_msg':"User not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))
    
    
#------------- Purchased Package Detail --------------       
@csrf_exempt
def package_detail(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        package = Purchased_subscriptions.objects.filter(user_id=user_id,is_valid=1).first()
        if package:
            package_id = Purchased_subscriptions.objects.filter(user_id=user_id,is_valid=1).first().package_id
            user = Users.objects.filter(id=user_id).first()
            name = Packages.objects.filter(id=package_id).first().name
            amount = Purchased_subscriptions.objects.filter(user_id=user_id,is_valid=1).first().amount
            from_date = Purchased_subscriptions.objects.filter(user_id=user_id,is_valid=1).first().from_date
            to_date = Purchased_subscriptions.objects.filter(user_id=user_id,is_valid=1).first().to_date
            pro_likes = Accessories.objects.first().pro_user_allowed_swipes
            duration_in_days = Packages.objects.filter(id=package_id).first().duration_in_days
            limit = Accessories.objects.filter(id=1).first()
            likes_left = limit.pro_user_allowed_swipes - Likes.objects.filter(user_id=user_id,date=datetime.now().date()).count()
            if user:
                if subscription:
                    return(JsonResponse({'error':True,'success_msg':"Succeeded",'name':name,'amount':amount,'from_date':from_date,'to_date':to_date,'pro_likes':pro_likes,'duration_in_days':duration_in_days,'likes_left':likes_left}))                   
                else:
                    return(JsonResponse({'error':True,'error_msg':"You have No Any Subscription"}))
            else:
                return(JsonResponse({'error':True,'error_msg':"User not found"}))
        else:
            return(JsonResponse({'error':True,'error_msg':"User have no any package"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))
    
#------------- Purchased Package Detail --------------       
@csrf_exempt
def cancel_subscription(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user = Users.objects.filter(id=user_id).first()
        subscription = Purchased_subscriptions.objects.filter(user_id=user_id,is_valid=1).first()
        if user:
            if subscription:
                subscription.is_valid = False
                user.pro = False
                subscription.save()
                user.save()
                profile = list(Profiles.objects.filter(user_id=user_id).values())
                if len(profile) > 0:
                    user = list(Users.objects.filter(id=user_id).values())[0]
                    data={}
                    data['error'] = False
                    data['success_msg'] = 'Succeeded'
                    user['profile'] = profile[0]
                    photo = []
                    user_profile_img = list(Profiles.objects.filter(user_id=user['id']).values('id','image'))[0]
                    photo.append(user_profile_img)
                    images = list(Photos.objects.filter(user_id=user['id']).values('id','image'))
                    if images:
                        for i in [0,1,2,3]:
                            if i < len(images):
                                photo.append(images[i])
                            else:
                                photo.append({})
                    else:
                        for i in [0,1,2,3]:
                            photo.append({})
                    user['images'] = photo
                data['user'] = user
                return JsonResponse(data, safe=False)
            else:
                return(JsonResponse({'error':True,'error_msg':"You have No Any Subscription"}))
        else:
            return(JsonResponse({'error':True,'error_msg':"User not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))


#------------- Expire Purchased Subscription --------------          
def subscription_expire():
    subscriptions = Purchased_subscriptions.objects.filter(is_valid=True)
    for sub in subscriptions:
        diff = sub.to_date - datetime.now().date()
        if diff.days < 0:
            sub.is_valid = False
            liked=Likes.objects.filter(user_id=sub.user_id)
            if liked > 0:
                for like in liked:
                    like.delete()
            user = Users.objects.filter(pk=sub.user_id).first()
            user.pro = False
            sub.save()
            user.save()

#------------- Update Age --------------          
def age():
    users = Users.objects.all()
    for user in users:
        age_update = Profiles.objects.filter(user_id=user.pk).first()
        days_in_year = 365.2425    
        user_age = int((date.today() - user.dob).days / days_in_year) 
        age_update.age = user_age
        age_update.save() 
                
#------------- Report User --------------
@csrf_exempt
def report(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        reported_user_id  = request.POST['reported_user_id']
        message = request.POST['message']
        User = Users.objects.filter(id=reported_user_id).first()
        favourite = Favourite.objects.filter(user_id=user_id,favourite_id=reported_user_id).first()
        if User:
            report = Reports(user_id = user_id,reported_user_id=reported_user_id,message=message,status=1)
            report.save()
            block_user = Users.objects.filter(id=reported_user_id).first()
            if block_user:
                if not Blocked_users.objects.filter(user_id=user_id,blocked_user_id=reported_user_id).first():
                    blocked = Blocked_users(user_id=user_id,blocked_user_id=reported_user_id)
                    blocked.save()
                    sbj = 'Someone has blocked you!!'
                    email = block_user.email
                    auto_msg = Auto_msg.objects.filter(id=1).first()
                    message =auto_msg.user_block
                    title='Someone Has Blocked You'
                    auto_message(sbj,email,title,message)
                    if favourite:
                        favourite.delete()
                    return(JsonResponse({'error':False,'success_msg':"succeeded"}))
            else:
                return(JsonResponse({'error':True,'error_msg':"users not found"}))
            return(JsonResponse({'error':False,'success_msg':"succeeded"}))
        else:
            return(JsonResponse({'error':True,'error_msg':"User not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))
    
#------------- User Report To Admin  --------------
@csrf_exempt
def admin_report(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        subject  = request.POST['subject']
        message = request.POST['message']
        User = Users.objects.filter(id=user_id).first()
        if User:
            report = Admin_reports(user_id=user_id,subject=subject,message=message,status=1)
            report.save()
            return(JsonResponse({'error':False,'success_msg':"succeeded"}))
        else:
            return(JsonResponse({'error':True,'error_msg':"User not found"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))
    
#------------- FAQ's --------------
@csrf_exempt
def faqs(request):
    if request.method == 'GET':
        faqs = list(Faqs.objects.all().values('question','answer'))
        return(JsonResponse({'error':False,'success_msg':"succeeded",'faq':faqs}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))
 

@csrf_exempt
def instant_msg(request):
    if request.method == 'POST':
        sender = request.POST['sender'] 
        receiver = request.POST['receiver']
        message = request.POST['message']
        group = Groups.objects.filter(Q(user_first=sender,user_second=receiver) | Q(user_first=receiver,user_second=sender)).first()
        if group:
            chat = Chat(sender=sender,receiver=receiver,message=message,group_id=group.id)
            chat.save()
            group.instant_msg_status = True
            group.save()
            return(JsonResponse({'error':False,'success_msg':"Message Send Successsfully"}))
        else:
            return(JsonResponse({'error':True,'error_msg':"Chat group not found!!"}))
    else:
        return(JsonResponse({'error':True,'error_msg':"Method not supported"}))
  
#------------- Charge Stripe --------------
def chargeStripe(token,amount):
    try:
        charge = stripe.Charge.create(
            amount=int(amount*100),
            currency="usd",
            source=token, 
        )
        return {"error": False, "charge": charge}
    except stripe.error.CardError as e:
        return {"error": True, "error_msg": str(e)}
        # Problem with the card
    except stripe.error.RateLimitError as e:
        # Too many requests made to the API too quickly
        return {"error": True, "error_msg": str(e)}
    except stripe.error.InvalidRequestError as e:
        # Invalid parameters were supplied to Stripe API
        return {"error": True, "error_msg": str(e)}
    except stripe.error.AuthenticationError as e:
        # Authentication Error: Authentication with Stripe API failed (maybe you changed API keys recently)
        return {"error": True, "error_msg": str(e)}
    except stripe.error.APIConnectionError as e:
        # Network communication with Stripe failed
        return {"error": True, "error_msg": str(e)}
    except stripe.error.StripeError as e:
        # Stripe Error
        return {"error": True, "error_msg": str(e)}
    except Exception as e:
        return {"error": True, "error_msg": 'something went wrong! please try again.'}


#------------- Distance --------------
def distance(lat_1,lon_1,lat_2,lon_2):
    # approximate radius of earth in km
    R = 6373.0
    lat1 = radians(lat_1)
    lon1 = radians(lon_1)
    lat2 = radians(lat_2)
    lon2 = radians(lon_2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    print("Result:", distance)
    print("Should be:", 278.546, "km")
    return distance

#------------- Convert base64 to image --------------
def base64_to_image(base64_string):
    format, imgstr = base64_string.split(';base64,') 
    ext = format.split('/')[-1]
    return ContentFile(base64.b64decode(imgstr), name=uuid4().hex + "." + ext)

def test(request):
    pushtest()
    dis = distance()
    return HttpResponse(1)
