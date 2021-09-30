from django.contrib import admin
from django.urls import path, include
from auth_login import views

urlpatterns = [
    path("", views.register, name="auth_register"),
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),


 ]


