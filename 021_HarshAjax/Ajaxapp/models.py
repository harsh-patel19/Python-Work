from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    








# class Student(models.Model):
#     name = models.CharField(max_length=20)
#     email = models.CharField(max_length=30)
#     phone = models.CharField(max_length=30)
#     age = models.IntegerField()

