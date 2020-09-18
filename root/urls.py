# Import the path function
from django.contrib import admin
from django.urls import path, include, re_path

# Import the views python file
from . import views

# Make a certain path call a certain view function
urlpatterns = [
 #   path('access/',include("django.contrib.auth.urls"),name='login'),
    path('',views.home,name="home"),
]