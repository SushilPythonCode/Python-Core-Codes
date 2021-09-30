from django.contrib import admin
from django.urls import path, include
from user_login import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("blog/", views.blog, name="addblog"),
    path("myblog/", views.blog_view, name="myblog"),
    path("delete/<int:id>", views.delete_blog, name="delete"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')


 ]


