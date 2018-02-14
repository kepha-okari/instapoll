from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required #restricting access to images for only registered users
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.index,name='home'),
    url(r'^new/group/',views.create_group, name='newGroup'),
    url(r'^new/question/',views.create_question, name='question'),
    url(r'^new/choice/',views.create_choice, name='choice'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

]
