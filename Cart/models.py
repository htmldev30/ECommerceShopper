from django.db import models

# Other App Models
from Products.models import Products
from User.models import UserProfile
# Create your models here.


class OrderItem(models.Model):
    product = models.OneToOneField(Products, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_ordered = models.DateTimeField(null=True)
    

    def __str__(self):
        return self.product.product_name


class Order(models.Model):
    ref_key = models.CharField(max_length=15)
    owner = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    # payment_details = models.ForeignKey(Payment, null=True)

    date_ordered = models.DateTimeField(auto_now_add=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        cart = Order.objects.get(owner=self.owner)
        items = cart.items.all()
        total_price = 0
        for item in items:
            total_price += item.product.product_price

        return total_price

    def get_cart_items_amount(self):
        cart = Order.objects.get(owner=self.owner)
        items = cart.items.all()
        total_items = 0
        for item in items:
            total_items += 1

        return total_items

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_key)


