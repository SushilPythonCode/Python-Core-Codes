from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    heading = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=50, blank=True)
    Content = models.TextField(max_length=1000, blank=True)
    image=models.ImageField(upload_to='images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
