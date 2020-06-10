from django.db import models
from .choices import Tag
from chefs.models import chef

# Create your models here.
class menu(models.Model):
    name = models.CharField(max_length=100)
    Ingredients = models.TextField()
    price = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    Tag = models.CharField(max_length=200,choices=Tag,default=None)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class special(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.TextField()
    description = models.TextField(blank=True)
    photo_dish = models.ImageField(upload_to='Photo/%Y/%m/%d/')
    
    def __str__(self):
        return self.name
