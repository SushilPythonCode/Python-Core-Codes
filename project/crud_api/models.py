from django.db import models

# Create your models here.

class Person(models.Model):
   name = models.CharField(max_length=100)
   birth_year = models.CharField(max_length=10)
   eye_color = models.CharField(max_length=10)
