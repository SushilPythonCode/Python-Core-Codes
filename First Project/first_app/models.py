from django.db import models

# Create your models here.
class Test(models.Model):
    name=models.CharField(max_length=255,unique=True)
    email = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'tbl_test'


class Register(models.Model):
    
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    comment=models.CharField(max_length=255)

        