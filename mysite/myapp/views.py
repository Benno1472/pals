from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import logout as lg
from .models import Post

# Create your views here.

def index(request):

    posts = Post.objects.all().order_by("-posted_time")

    context = {'user': request.user, "posts": posts}
    return render(request, "myapp/index.html", context)

def create_post(request):

    if request.user.is_authenticated:
        return render(request, "myapp/create_post.html")
    else:
        return redirect('login')

def profile(request, name):

    if request.user.is_authenticated:

        user = get_object_or_404(User, username=name)
        posts = Post.objects.filter(user=user).order_by('-posted_time')

        context = {'name': name, 'user': request.user, "posts": posts}
        return render(request, "myapp/profile.html", context)
    else:
        return redirect('login')

def login(request):
    context = {}
    return render(request, "myapp/registration/login.html", context)

def create(request):
    # default User Creation Form from django
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # if the form is valid
        if form.is_valid():
            # create the user and store
            form.save()
            # redirect to the success page
            return redirect("/myapp/accounts/create/success")
    else:
        form = UserCreationForm()


    context = {'form':form}
    return render(request, "registration/create.html", context)

def success(request):
    context = {}
    return render(request, "registration/success.html", context)

def create_post_submit(request):
    if request.user.is_authenticated:
        body = request.POST['body']
        # y
        q = Post(post_text=body, posted_time=timezone.now(), id=None, user=request.user)
        q.save()
    return redirect('index')

def logout(request):
    lg(request)
    return redirect('index')

def search(request):
    pass