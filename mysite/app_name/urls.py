from django.urls import path

from app_name import views

urlpatterns = [
    path('', views.index, name='index'),
]
