from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=100)