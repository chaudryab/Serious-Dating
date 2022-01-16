from django.shortcuts import render
from django.contrib import messages
from api.models import *
from adminn.models import *
from chat.models import *
import os
from pathlib import Path



#---------------- Insert Database ----------------
def insert_db(request):
    admin_token=Admin_token()
    auto_msg=Auto_msg()
    terms=Terms_and_conditions()
    policy=Privacy_policies()
    links=App_links()
    accessories=Accessories()
    admin_token.save()
    auto_msg.save()
    terms.save()
    policy.save()
    links.save()
    accessories.save()
    messages.success(request, 'Database Insert Successfully !!')
    return render(request,'success.html')

#------------- Insert Emoji In DB --------------
def insert_emoji(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    for subdir, dirs, files in os.walk(os.path.join(BASE_DIR, 'staticfiles/emojis')):
        for file in files:
            path = os.path.join(subdir, file)
            exact_name = path.split('emojis')[1]
            emojis = exact_name[1:]
            emoji = Emoji(emoji=emojis)
            emoji.save()
    messages.success(request, 'Successfully Insert Emojies in database !!')
    return render(request,'success.html')

#------------- Insert Gifts In DB --------------
def insert_gifts(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    for subdir, dirs, files in os.walk(os.path.join(BASE_DIR, 'staticfiles/gifts')):
        for file in files:
            path = os.path.join(subdir, file)
            exact_name = path.split('gifts')[1]
            gifts = exact_name[1:]
            gifts = Gifts(gift=gifts)
            gifts.save()
    messages.success(request, 'Successfully Insert GIF in database !!')
    return render(request,'success.html')
