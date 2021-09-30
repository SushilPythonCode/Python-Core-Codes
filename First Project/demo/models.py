from django.db import models

# Create your models here.

class Teacher(models.Model):
    tname = models.CharField(max_length = 100)
    
class Student(models.Model):
     stuname = models.CharField(max_length = 100)
     pteacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)


class Section(models.Model):
    secname = models.CharField(max_length = 100)
    pstudent_section = models.ForeignKey(Student, on_delete = models.CASCADE)
    pteacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)



