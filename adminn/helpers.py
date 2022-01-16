from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

#------------- Forget Password --------------
def send_admin_forget_password_mail(email,token):
    subject = 'your change password link'
    link = 'https://serious-dating-ltd.herokuapp.com/adminn/reset_pwd/'+token
    # link = 'http://192.168.1.29:8000/adminn/reset_pwd/'+token
    html_message = render_to_string('mail_template.html', {'link': link})
    plain_message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message)
    return True

#------------- Reply Complain --------------
def reply_complain_mail(email,reply):
    subject = 'Respose from serious dating of your complain'
    html_message = render_to_string('reply_complain_template.html', {'reply': reply})
    plain_message = strip_tags(html_message)
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