from django.contrib import admin
from django.urls import path, include
from first_app import views
app_name = 'first_app'
urlpatterns = [
    path("", views.index, name='first_app'),
    # path("about", views.about, name='about'),
    # path("services", views.services, name='services'),
    # path("contact", views.contact, name='contact'),
    path("add/", views.add, name='add'),
    path("register/", views.register, name='register'),
    path("edit/<int:id>", views.edit, name='edit'),
    path("update/<int:id>", views.updateuser, name='update'),
    path("delete/<int:id>", views.delete, name='delete')


]


