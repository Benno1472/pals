from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.all_posts, name="all_posts"),
    path('profile/', views.my_profile, name="my_profile"),
    path('create/', views.create_post, name="create_post"),
    path('registration/login/', views.login, name="login")
]