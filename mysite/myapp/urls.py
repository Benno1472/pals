from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.all_posts, name="all_posts"),
    path('profile/<slug:name>', views.profile, name="profile"),
    path('create/', views.create_post, name="create_post"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/create', views.create, name="create"),
    path('accounts/create/success', views.success, name="success"),
    path('accounts/logout', views.logout, name="logout")
]