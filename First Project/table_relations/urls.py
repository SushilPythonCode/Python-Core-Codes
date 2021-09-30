from django.contrib import admin
from django.urls import path, include
from table_relations import views

urlpatterns = [
    path("", views.index, name='table'),
]