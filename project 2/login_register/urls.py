from django.contrib import admin
from django.urls import path, include
from login_register import views

from django.contrib.auth.views import LogoutView

app_name = 'login_register'


urlpatterns = [
  
    path("", views.IndexView.as_view(), name='index'),
    path("register/", views.Register.as_view(), name='register'),
    path("login/", views.Login.as_view(), name='login'),
    path("dashboard/", views.dashboard.as_view(), name="dashboard"),
    path("contact/", views.contact.as_view(), name='contact'),
    path("about/", views.about.as_view(), name='about'),
    path("edit/<int:id>", views.edit.as_view(), name='edit'),
    path("update/", views.updateuser.as_view(), name='update'),
    path("delete/<int:id>", views.delete.as_view(), name='delete'),
    path('logout/', LogoutView.as_view(next_page='/login'), name='Logout'),

# GM Urls-----------------------------------------------------------------
    path("Gmlist/", views.Gm_list.as_view(), name="gmlist"),

    path("addgm/", views.Gm_view.as_view(), name="genralmanager"),







 ]


