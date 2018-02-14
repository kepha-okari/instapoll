from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.db import models
from .forms import GroupForm,QuestionForm,ChoiceForm
from django.contrib.auth.models import User
from .models import Question, Choice
import datetime as dt

from wsgiref.util import FileWrapper
# import mimetypes
from django.conf import settings
import os

# Create your views here.



def index(request):
    title = 'Instapoll'
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# output = ','.join([q.question_text for q in latest_question_list])
	# return HttpResponse(output)
    return render(request, 'index.html',{"title":title})



@login_required(login_url='/accounts/login')
def create_group(request):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user

    if request.method == 'POST':
        form = ChoiceForm(request.POST, request.FILES)
        if form.is_valid:
            k = form.save(commit=False)
            k.user = current_user
            k.save()
            return redirect(index)

    else:
        form = ChoiceForm()
    return render(request, 'new-group.html', {"form":form})


@login_required(login_url='/accounts/login')
def create_question(request):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid:
            k = form.save(commit=False)
            k.user = current_user
            k.save()
            return redirect(index)

    else:
        form = QuestionForm()
    return render(request, 'new-poll.html', {"form":form})

@login_required(login_url='/accounts/login')
def create_choice(request):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user

    if request.method == 'POST':
        form = ChoiceForm(request.POST, request.FILES)
        if form.is_valid:
            k = form.save(commit=False)
            k.user = current_user
            k.save()
            return redirect(index)

    else:
        form = ChoiceForm()
    return render(request, 'new-poll.html', {"form":form})
