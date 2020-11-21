from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    context = {}
    return render(request, "myapp/index.html", context)

def create_post(request):
    return HttpResponse("Hello world. You are at the create post page.")

def my_profile(request):
    return HttpResponse("Hello world. You are at the my profile page.")

def all_posts(request):
    return HttpResponse("Hello world. You are at the all posts page.")

def login(request):
    context = {}
    return render(request, "myapp/registration/login.html", context)

def create(request):
    # default User Creation Form from django
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, "registration/create.html", context)

def logout(request):
    # logout page
    context = {}
    return render(request, "registration/logout.html", context)