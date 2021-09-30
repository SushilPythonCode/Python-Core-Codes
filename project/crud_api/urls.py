from django.urls import path
from crud_api import views
from .views import *
urlpatterns = [
   path('getlist/',Personlist.as_view()),
 

]