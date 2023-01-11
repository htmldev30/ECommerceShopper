from django.db import models
from django.contrib.auth.models import User
from Products.models import Products
# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_bio = models.CharField(max_length=50)
    user_pic = models.ImageField(upload_to="user_image")
    user_background = models.ImageField(upload_to="user_image_back")
    product = models.ManyToManyField(Products, blank=True)

    def __str__(self):
        return str(self.user)






