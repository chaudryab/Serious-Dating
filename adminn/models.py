from django.db import models
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Admin_token(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class Auto_msg(models.Model):
    id = models.AutoField(primary_key=True)
    welcome = models.TextField(null=True)
    matching = models.TextField(null=True)
    breakup = models.TextField(null=True)
    user_block = models.TextField(null=True)
    admin_block = models.TextField(null=True)
    admin_unblock = models.TextField(null=True)
    user_delete = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField(null=True)
    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

class Editor(models.Model):
    body=RichTextField(blank=True,null=True)
 
   
