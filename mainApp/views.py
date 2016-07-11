from django.shortcuts import render
from django.contrib import auth

# Create your views here.

def index(request):
    #user=auth.get_user(request).username
    return render(request,'index.html' )

def page2(request):
    #user=auth.get_user(request).username
    return render(request,'page2.html' )