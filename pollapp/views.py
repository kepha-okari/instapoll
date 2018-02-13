from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from .models import Question, Choice
import datetime as dt



# Create your views here.



def index(request):
    title = 'Instapoll'
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# output = ','.join([q.question_text for q in latest_question_list])
	# return HttpResponse(output)
    return render(request, 'index.html',{"title":title})
