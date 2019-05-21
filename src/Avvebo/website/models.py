from django.db import models
from django.contrib.auth.models import User as DjangoUser
# makemigrations
# then migrate
# Create your models here.
class AvveboProfile(models.Model):
    user = models.ForeignKey(DjangoUser,on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True)
    reward_points = models.IntegerField(default=0)
    member_since = models.DateField(auto_now_add=True)
    id = models.CharField(max_length=50, unique=True, null=False)  # api_id string
    pic_url = models.CharField(max_length=50)
    isTalent = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    
    def __str__(self):  # __unicode__ on Python 2
        return self.id
    
class SocialMedia(models.Model):
    talent = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=80)
    
    def __str__(self):
        return self.talent

class TalentContent(models.Model):
    talent = models.ForeignKey(User, on_delete=models.CASCADE)
    video_url = models.CharField(max_length=50)
    date_uploaded = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.video_url


class Venue(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    member_since = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.id
