from django.db import models

#------------- Groups Table --------------
class Groups(models.Model):
    match = models.OneToOneField("api.Matchings",on_delete=models.CASCADE)
    user_first = models.IntegerField()
    user_second = models.IntegerField()
    status = models.BooleanField(default=True)
    blocked_by_user = models.IntegerField(null=True)
    unblock_by_user = models.IntegerField(null=True)
    instant_msg_status = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

#------------- Emojis Table --------------
class Emoji(models.Model):
    id = models.AutoField(primary_key=True)
    emoji = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

#------------- Gifts Table --------------
class Gifts(models.Model):
    id = models.AutoField(primary_key=True)
    gift = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
 
#------------- Chat Table --------------   
class Chat(models.Model):
    sender = models.IntegerField()
    receiver = models.IntegerField()
    message = models.TextField(null = True)
    image = models.ImageField(upload_to='profile/', null=True)
    video = models.FileField(upload_to='chat_videos/', null=True)
    voice = models.FileField(upload_to='chat_voices/', null=True)
    svg = models.CharField(max_length=200, default=None, null=True)
    group = models.ForeignKey(Groups, related_name='group', on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    call_type = models.IntegerField(null=True)
    call_status = models.IntegerField(null=True)
    ended_by = models.IntegerField(null=True)
    address = models.CharField(max_length=255,null=True)
    latitude = models.CharField(max_length=255,null=True)
    longitude = models.CharField(max_length=255,null=True)
    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    deleted_by_user1 = models.IntegerField(default=False)
    deleted_by_user2 = models.IntegerField(default=False)
    delete_chat_by_user1 = models.IntegerField(default=False)
    delete_chat_by_user2 = models.IntegerField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
# class Notifications(models.Model):
#     notiTo = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='my_noti')
#     notiFrom = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='noti_by_me')
#     notiMessage = models.CharField(max_length=255)
#     type = models.CharField(max_length=100)
#     post_id = models.IntegerField(null=True)
#     reply_id = models.IntegerField(null=True)
#     comment_id = models.IntegerField(null=True)
#     seen = models.BooleanField(default=False)
#     follow = models.BooleanField(default=False)
#     partnership = models.BooleanField(default=False)
#     connect_id = models.IntegerField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

    



    
