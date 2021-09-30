from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
roleID =(
    ("Admin", 1),
    ("General Manager", 2),
    ("Branch Manager", 3),
    ("Relational Manager", 4),
    ("Normal user" , 5 )
  
)

class User(AbstractUser):

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True, unique=True)
    mobile_no = models.CharField(max_length=100, blank=True, unique=True)
    password = models.CharField(max_length=100, blank=True)
    password2 = models.CharField(max_length=100, blank=True)        
    username = models.CharField(max_length=100, blank=True, unique=True)
    usertype= models.PositiveIntegerField(choices=roleID, default=1)



#http://127.0.0.1:8000/api/getuserlist
