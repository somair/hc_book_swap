from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from books.views import index
from login.forms import UserForm

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            print(form.errors)
    return render(request, 'registration/register.html', {'form': form})