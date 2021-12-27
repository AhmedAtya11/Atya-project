from django.urls import path
from django.contrib import admin
from dthms_app import views

urlpatterns = [
    path('home', views.home, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('team', views.team, name='team'),
]