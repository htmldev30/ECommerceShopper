from django.db import models
from django.contrib.auth.models import User
from Products.models import Products
# Create your models here.



'''def total_price(self):
        user_related = Cart.objects.get(user=self.user)
        user_cart = user_related.items.all()
        total_price = 0
        for item in user_cart:
            total_price +=  item.product_price
        return total_price


    def time_added(self, items):
        now = timezone.now()

        time_added = now - self.creation_date

        if time_added == 0 and time_added.seconds >= 0 and time_diff.seconds < 60:
            seconds = time_added.seconds
            
            if seconds < 1:
                return " seconds ago"

        
        if time_added.days == 0 and time_added.seconds >= 60 and time_added.seconds < 3600:
            minutes = math.floor(time_added/60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:

                return str(minutes) + " minutes ago"

        if time_added.days == 0 and time_added.seconds > 3600 and time_added.seconds < 86400:
            hours = math.floor(time_added.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago" 

            else:
                return str(hours) + " hours ago"


        if time_added.days >= 30 and time_added.day < 365:
            months = math.floor(time_added.days/30)

            if months == 1:
                return str(months) + " month ago"

            else:

                return str(months) + " months ago"


        if time_added.days > 365:
            years = math.floor(time_added/365)

            if years == 1:
                return str(years) + " year ago"

            else:

                return str(years) + " years ago"      

        

    class Meta:
        verbose_name = ('Cart')
        verbose_name_plural = ("Carts")
        ordering = ("-creation_date",)'''


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_bio = models.CharField(max_length=50)
    user_pic = models.ImageField(upload_to="user_image")
    user_background = models.ImageField(upload_to="user_image_back")
    product = models.ManyToManyField(Products, blank=True)

    def __str__(self):
        return str(self.user)






