from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    state = models.CharField(max_length=30, blank=True)


class Product(models.Model):
    product_name = models.CharField(max_length=30, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    category_name = models.CharField(max_length=30, blank=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
