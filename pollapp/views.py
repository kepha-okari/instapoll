from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.db import models
from .forms import GroupForm,QuestionForm,ChoiceForm,VoteForm
from django.contrib.auth.models import User
from .models import Question, Choice, Vote
import datetime as dt

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

# Create your views here.



def index(request):
    title = 'Instapoll'
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# output = ','.join([q.question_text for q in latest_question_list])
	# return HttpResponse(output)
    questions = Question.get_questions

    return render(request, 'index.html',{"title":title, "questions":questions})



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
def create_choice(request, question_id):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user

    if request.method == 'POST':
        qsn_id= Question.objects.get(id=question_id)
        form = ChoiceForm(request.POST, request.FILES)
        if form.is_valid:
            k = form.save(commit=False)
            k.user = current_user
            k.question =qsn_id
            k.save()
            return redirect(index)

    else:
        form = ChoiceForm()
    return render(request, 'new-poll.html', {"form":form})

# @login_required(login_url='/accounts/login')
# def vote(request):
#     '''
#     '''
#     current_user = request.user
#
#     # qsn_id= Question.objects.get(id=question_id)
#
#     if request.method == 'POST':
#         form = VoteForm(request.POST, request.FILES)
#         if form.is_valid:
#             k = form.save(commit=False)
#             k.user = current_user
#             k.save()
#             return redirect(index)
#
#     else:
#         form = VoteForm()
#     return render(request, 'vote.html', {"form":form})

#vote for a question
@login_required(login_url='/accounts/login')
def vote(request,choice_id):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user

    chosen = Choice.get_specific_choice(choice_id)

    question = Question.get_specific_question(chosen.question.id)

    voted = Vote(choice=chosen , question=question , user=current_user)
    voted.save()

    # return redirect('view_results' id=question.id) #return the results
    return redirect('home')




#display choices of a question
@login_required(login_url='/accounts/login')
def cast_vote(request,question_id):
    '''
    View function to display choices of a question
    '''
    current_user = request.user

    #fetch specific question
    question = Question.get_specific_question(question_id)

    #fetch all the choices given for a given question
    choices = Choice.get_question_choices(question_id)


    return render(request, 'vote-question.html', {"question":question,"choices":choices})


#**************************************************************viewing details***************************************************************

def view_questions(request):
    # images = Image.get_images()
    current_user = request.user
    title = 'Poll Topics'

    questions = Question.get_questions


    return render(request, 'view-questions.html', {"title": title, "questions": questions})


#*******************************************************************check Results*****************************************************************

@login_required(login_url='/accounts/login')
def view_results(request,question_id):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user

    poll = Question.get_specific_question(question_id)

    # Collect all votes casted
    question= Vote.objects.filter(question=question_id)
    voters = len(question)

    # fetch all possible choices for a question
    choices = Choice.get_question_choices(question_id)
    options =len(choices)
    votes_for = {}
    #count votes each choice has
    for answer in choices:
        vote_count = len(Vote.objects.filter(question=question_id,choice=answer.id))
        votes_for[answer.id] = vote_count
        score = voters


    return render(request, 'results.html', {"poll":poll,"voters":voters,"options":options,"choices":choices,"votes_for":votes_for})
