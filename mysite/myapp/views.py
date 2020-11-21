from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from .models import Post

# Create your views here.

def index(request):

    posts = Post.objects.all().order_by('posted_time')

    context = {'user': request.user, "posts": posts}
    return render(request, "myapp/index.html", context)

def create_post(request):
    return render(request, "myapp/create_post.html")

def profile(request, name):

    posts = Post.objects.filter(post_owner_name=name).order_by('-posted_time')

    context = {'name': name, 'user': request.user, "posts": posts}
    return render(request, "myapp/profile.html", context)

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

def create_post_submit(request):
    body = request.POST['body']
    q = Post(post_text=body, post_owner_name=request.user)
    q.save()
    return redirect('index')


def logout(request):
    # logout page
    context = {}
    return render(request, "registration/logout.html", context)