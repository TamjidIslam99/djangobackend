from django.db import models

# Create your models here.
class Student1(models.Model):
    stuname= models.CharField(max_length=100)
    email=models.EmailField(max_length=100)