from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.

class Group (models.Model):
    photo = models.ImageField(upload_to = 'groups/', null=True,blank=True)
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User)

class Question(models.Model):
    question_title = models.CharField(max_length=200)
    instructions = models.CharField(max_length=400, blank=True,null=True)
    date_started = models.DateTimeField(auto_now_add=True, null=True)
    date_closing = models.DateTimeField(null=True)
    group = models.ForeignKey(Group,null =True,blank=True, on_delete=models.CASCADE)
    vote_count = models.IntegerField(default=0)

    @classmethod
    def get_questions(cls):
        questions = cls.objects.all()
        return questions

    @classmethod
    def get_specific_question(cls,question_id):
        question = cls.objects.get(id=question_id)
        return question



class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    vote_cast = models.IntegerField(default=0)
    user = models.ForeignKey(User,null =True,blank=True,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,null =True,blank=True, on_delete=models.CASCADE)


    @classmethod
    def get_specific_choice(cls,choice_id):
        choice = cls.objects.get(id=choice_id)
        return choice


    @classmethod
    def get_question_choices(cls,question_id):
        choices = cls.objects.filter(question=question_id)
        return choices


class Profile(models.Model):
    photo = models.ImageField(upload_to = 'profiles/', null=True,blank=True)
    email = models.EmailField(max_length=70,blank=True)
    phone = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Follow(models.Model):
    '''
    Class that store a User and Profile follow group precedings
    '''
    user = models.ForeignKey(User,null=True,blank=True  )
    group = models.ForeignKey(Group,null=True,blank=True)
