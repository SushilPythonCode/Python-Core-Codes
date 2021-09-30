
from django.contrib import admin
from django.urls import path
from payments import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('charge/', views.charge, name='charge'),


]
