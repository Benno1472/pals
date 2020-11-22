from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post, Comment
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block, FriendshipRequest
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


def post_image_view(request):
    if request.method == 'POST':
        form = Post_Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = Post_Form()
    return render(request, 'create_post.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
# or friend_request.reject()


def show_friends(request):
    if request.user.is_authenticated:
        User = get_user_model()
        users = User.objects.all()
        context = {'friends_list': dict(
            Friend.objects.friends(request.user)), "users": users}
        return render(request, "friends.html", context)


def accept_friend_request(user_num):
    friend_request = FriendshipRequest.objects.get(to_user=user_num)
    friend_request.accept()
# Create your views here.


def send_friend_request(request, receiving_user, message_txt):

    Friend.objects.add_friend(
        request.user,
        receiving_user,
        message=message_txt
    )


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

        # check if credidentials are valid (returns NoneType if not valid )
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
            # create a new user and store it in the database
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

def delete_check(request):
    # take the user to the confirm deletion page
    context = {}
    return render(request, "registration/delete.html", context)

def delete_user(request):
    # delete the user account from all databases
    context = {}
    # check authentication
    if request.user.is_authenticated:
        # get the username
        username = request.user.username
        # delete the user
        u = User.objects.get(username=username)
        u.delete()
    # redirect back to the home page (logged out view)
    return redirect('index')


def create_post_submit(request):
    if request.user.is_authenticated:
        body = request.POST['body']
        image = request.POST['image']
        # y
        q = Post(post_text=body, post_img=image, posted_time=timezone.now(),
                 id=None, user=request.user)
        q.save()
    return redirect('index')


def logout_page(request):
    logout(request)
    return redirect('index')

def delete_post(request, post_key):
    q = get_object_or_404(Post, pk=post_key)

    if request.user == q.user:
        q.delete()

    return redirect('index')


def search(request):
    pass
