from django.db import models
from chat.models import *


# Create your models here.

#---------------------------------------- Parent Tables -------------------------------------------

#------------- Users Table --------------
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255,null=True)
    gender = models.CharField(max_length=255)
    dob = models.DateField()
    pro = models.BooleanField(default=0)
    google_key = models.CharField(max_length=255,null=True)
    facebook_key = models.CharField(max_length=255,null=True)
    token = models.CharField(max_length=255,null=True)
    expo_token = models.CharField(max_length=255,null=True)
    status = models.BooleanField(default=0)
    is_deleted = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
#------------- Packages Table --------------
class Packages(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12,decimal_places=2)
    duration_in_days = models.IntegerField()
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


#---------------------------------------- One To One Relation with User -------------------------------------------

#------------- Users Profile Table --------------
class Profiles(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Users,on_delete=models.CASCADE,related_name="profile")
    age = models.IntegerField()
    image = models.ImageField(default='serious_dating/profile/default_pic.png',upload_to='profile/', null=True)
    profession = models.CharField(max_length=255,null=True)
    education = models.CharField(max_length=255,null=True)
    country = models.CharField(max_length=255,null=True)
    marital_status = models.CharField(max_length=255,null=True)
    height = models.CharField(max_length=255,null=True)
    smoke = models.BooleanField(null=True,default=None)
    drink = models.BooleanField(null=True,default=None)
    children = models.BooleanField(null=True,default=None)
    address = models.CharField(max_length=255,null=True)
    bio = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
#------------- Users Location Table --------------
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Users,on_delete=models.CASCADE,related_name="location")
    latitude = models.DecimalField(max_digits=9, decimal_places=6,null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    
#---------------------------------------- Many To One Relation with User --------------------------------------------

#------------- Photos Profile Table --------------
class Photos(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='photo')
    image = models.ImageField(upload_to='profile/',null=True,default=None,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

#------------- Blocked Users Table --------------
class Blocked_users(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='block_user')
    blocked_user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='blocked_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

#------------- Reports Users Table --------------
class Reports(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='report_user')
    reported_user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='reported_user')
    message = models.CharField(max_length=255)
    status = models.BooleanField(default=0)
    response = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
#------------- Reports Admin Table --------------
class Admin_reports(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='user_report_admin')
    subject = models.IntegerField()
    message = models.CharField(max_length=255)
    status = models.BooleanField(default=0)
    response = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
#------------- Likes Table --------------
class Likes(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
#------------- Matchings Table --------------
class Matchings(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='matching_user')
    match = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='matched_user')
    liked_by_user1 = models.BooleanField(default=0)
    liked_by_user2 = models.BooleanField(default=0)
    status = models.BooleanField(default=0)
    deleted_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
#------------- Dislike Table --------------
class Dislike(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='disliking_user')
    dislike = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='disliked_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
#------------- Favourite Table --------------
class Favourite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='favouriting_user')
    favourite = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='favourited_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
#------------- Filter Table --------------
class Filter(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    age_from = models.IntegerField(null=True)
    age_to = models.IntegerField(null=True)
    country = models.CharField(max_length=255,null=True)
    marital_status = models.CharField(max_length=255,null=True)
    gender = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

#---------------------------------------- Many To One Relation with User And Packages --------------------------------

#------------- Purchased Subscriptions Table --------------
class Purchased_subscriptions(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='subscriptions')
    package = models.ForeignKey(Packages, on_delete=models.CASCADE,related_name='purchased_packages')
    transection_id = models.CharField(max_length=225)
    amount = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    from_date = models.DateField()
    to_date = models.DateField()
    is_valid = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
#------------- Visited Users Table --------------
class Visited_Users(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='visiting_user')
    visited_user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='visited_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

  
#---------------------------------------- Without Relation Tables -----------------------------------------------------

#------------- App Links Table --------------
class App_links(models.Model):
    id = models.AutoField(primary_key=True)
    ios = models.TextField(max_length=255)
    android = models.TextField(max_length=255)

#------------- Accessories Table --------------
class Accessories(models.Model):
    id = models.AutoField(primary_key=True)
    free_user_allowed_swipes = models.IntegerField(default=0)
    pro_user_allowed_swipes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

#------------- Terms And Conditions Table --------------
class Terms_and_conditions(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

#------------- Privacy Policies Table --------------
class Privacy_policies(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
#------------- Faqs Table --------------
class Faqs(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField(max_length=255)
    answer = models.TextField(max_length=255)
    is_deleted = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
