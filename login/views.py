from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

def register(request):
    return HttpResponse("register")

def login(request):
    return HttpResponse("Login")
    
def logout(request):
    return HttpResponse("Logout")