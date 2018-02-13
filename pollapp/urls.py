from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required #restricting access to images for only registered users
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.index,name='how'),
    # url(r'^profile/',views.profile, name='profileView'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$',views.index ,name ='home')

]
