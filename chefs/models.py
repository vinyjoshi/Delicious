from django.db import models
 

# Create your models here.
class chef(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    DOB = models.DateTimeField(blank=False)
    designation = models.CharField(max_length=100)
    photo_chef = models.ImageField(upload_to='Photos/%Y/%m/%d/')
    join_date = models.DateTimeField(auto_now_add=True)
    facebook_link = models.CharField(max_length=100,blank=True)
    instagram_link = models.CharField(max_length=100,blank=True)
    linkedIn_link = models.CharField(max_length=100,blank=True)
    twitter_link = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name