from django.contrib import admin
from django.urls import path, include
from Auth import views
urlpatterns = [
    path("", views.register, name="auth"),
    path("login", views.login, name='login'),
    # path("dashboard", views.dashboard, name='dashbaord'),
    # path("test", views.test ,name='test'),



   


]


