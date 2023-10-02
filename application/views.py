from django.shortcuts import render, redirect
from django.http import HttpResponse
from application.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.


def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def gallery(request):
    return render(request,'gallery.html')

def services(request):
    return render(request,'services.html')

def digital(request):
    return render(request,'digital.html')

def contact(request):
    return render(request,'contact.html')
def login_user(request):
    return render(request, 'login.html')
    