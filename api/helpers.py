from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.template import loader

#------------- Email Verification --------------
def email_verifications(email, token):
    subject = 'Email Verification Code'
    html_message = render_to_string('otp.html', {'token': token})
    plain_message = ''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message)
    return True


#------------- Auto Mail --------------
def auto_message(sbj,email,title,message):
    subject = sbj
    html_message = render_to_string('auto_msg.html', {'title':title,'message': message})
    plain_message = ''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message)
    return True

#------------- Matching Mail --------------
def match_mail(sbj,email_1,email_2,title,message):
    subject = sbj
    html_message = render_to_string('auto_msg.html', {'title':title,'message': message})
    plain_message = ''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_1,email_2]
    send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message)
    return True