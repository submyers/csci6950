from django.shortcuts import render
from django.http import HttpResponse
from os.path import join

def home(response):
    return render(response,join("home","index.html"))