from django.db import models
from .choices import *

# Create your models here.
class booking(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    date = models.CharField(max_length=200)    
    time = models.CharField(max_length=200)
    people = models.CharField(max_length=200)
    user_id = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.name
    
class Inquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=False)
    user_id = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.name