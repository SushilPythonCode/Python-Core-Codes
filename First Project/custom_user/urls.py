from django.contrib import admin
from django.urls import path, include
from custom_user import views

urlpatterns = [
    path("", views.register, name="custom"),
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),




]


