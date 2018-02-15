from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Group,Profile,Question,Choice



class GroupForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to create Group
    '''
    class Meta:
        model = Group
        fields = ['photo','name']

#*************************************************************************************************************

class QuestionForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to post a poll
    '''
    class Meta:
        model = Question
        fields = ['question_title', 'instructions','date_closing']


#************************************************** Enter A Choice **********************************************


class ChoiceForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to post a poll
    '''
    class Meta:
        model = Choice
        fields = ['choice_text']


#************************************* SET UP A PROFILE **********************************************************


class ProfileForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to update profile
    '''
    class Meta:
        model = Profile
        fields = ['photo','email','phone']


#***********************************************************ACTUAL VOTING****************************************

class VoteForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to vote
    '''
    class Meta:
        model = Choice
        fields = ['vote_cast']
