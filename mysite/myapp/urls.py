from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<slug:name>', views.profile, name="profile"),
    path('create/', views.create_post, name="create_post"),
    path('create/submit/', views.create_post_submit, name="create_post_submit"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/create', views.create, name="create"),
    path('accounts/logout', views.logout_page, name="logout")
]