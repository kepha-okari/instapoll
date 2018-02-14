from django.db import models
import datetime as dt
from django.contrib.auth.models import User
# Create your models here.



class Question(models.Model):
    question_title = models.CharField(max_length=200)
    date_started = models.DateTimeField(auto_now_add=True, null=True)
    date_closing = models.DateTimeField(auto_now_add=True,null=True)
    vote_count = models.IntegerField(default=0)



class Group (models.Model):
    photo = models.ImageField(upload_to = 'groups/', null=True,blank=True)
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User)


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    users = models.ForeignKey(User,null =True,blank=True,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,null =True,blank=True, on_delete=models.CASCADE)
    group = models.ForeignKey(Group,null =True,blank=True, on_delete=models.CASCADE)


class Profile(models.Model):
    photo = models.ImageField(upload_to = 'profiles/', null=True,blank=True)
    email = models.EmailField(max_length=70,blank=True)
    phone = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Follow(models.Model):
    '''
    Class that store a User and Profile follow group precedings
    '''
    user = models.ForeignKey(User,null=True,blank=True  )
    group = models.ForeignKey(Group,null=True,blank=True)
