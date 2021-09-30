from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.

# class UserRegister:  creatig object to pass data dynamicaly to html page without database

#     id: int
#     fname: str
#     lname: str
#     email: str
#     comment: str

class UserRegister(models.Model):

    fname = models.CharField(max_length=100,blank=True)
    lname = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=100,blank=True)
    comment= models.CharField(max_length=1000,blank=True)

    class Meta:
        managed = True
        db_table = 'tbl_user_registration'