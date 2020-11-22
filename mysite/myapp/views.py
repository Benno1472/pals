from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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


def login_page(request):
    if request.method == 'POST':
        # get post data
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        # check if user exists
        if user is not None:
            # login the user
            login(request, user)
            # redirect the user to the home page ('index' doesn't work for some reason)
            return redirect('/myapp')
        else:
            # if user doesn't exist send error message (not working for some reason)
            messages.info(request, 'Username or Password is incorrect')

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
            # success message
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            # redirect to login page
            return redirect("/myapp/accounts/login")
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, "registration/create.html", context)


def create_post_submit(request):
    if request.user.is_authenticated:
        body = request.POST['body']
        # y
        q = Post(post_text=body, posted_time=timezone.now(),
                 id=None, user=request.user)
        q.save()
    return redirect('index')


def logout_page(request):
    logout(request)
    return redirect('index')

def search(request):
    pass