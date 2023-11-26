from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

class Boook(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)