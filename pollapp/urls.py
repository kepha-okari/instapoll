from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required #restricting access to images for only registered users
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.index,name='home'),
    url(r'^new/group/',views.create_group, name='newGroup'),
    url(r'^new/question/',views.create_question, name='question'),
    url(r'^view/questions/',views.view_questions, name='viewQuestion'),
    url(r'^cast/vote/(\d+)',views.cast_vote, name='castVote'),
    url(r'^new/choice/(\d+)',views.create_choice, name='choice'),
    url(r'^vote/(\d+)',views.vote, name='vote'),
    url(r'^results/(\d+)',views.view_results, name='viewResults'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

]
