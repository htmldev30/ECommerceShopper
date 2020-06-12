from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
import uuid
# Create your models here.

CATEGORIES = (
    ("Shirts", "Shirts"),
    ("Long Sleeves", "Long Sleeves"),
    ("Hoodies", "Hoodies"),
    ("Beanies", "Beanies"),
    ("Others", "Others"),
)



# Cateogries 
class Category(models.Model):
    category_name = models.CharField(max_length=20, choices=CATEGORIES, default='Shirt')
    category_slug = models.SlugField(max_length=40, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

def pre_save_post_receiver_category(sender, instance, *args, **kwargs):
    category_slug = slugify(instance.category_name)
    category_exists = Category.objects.filter(category_slug=category_slug).exists()
    if category_exists:
        category_slug = "%s_%s" %(category_slug, instance.id)

    instance.category_slug = category_slug


pre_save.connect(pre_save_post_receiver_category, sender=Category)


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField(default=0)
    product_description = models.CharField(max_length=100)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image_prev = models.ImageField(upload_to="prev_images")
    product_image = models.ImageField(upload_to="product_images")
    time_released = models.DateTimeField(auto_now_add=True)
    product_slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    
    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    product_slug = slugify(instance.product_name)
    exists = Products.objects.filter(product_slug=product_slug).exists()
    if exists:
        product_slug = "%s_%s" %(product_slug, instance.id)

    instance.product_slug = product_slug

pre_save.connect(pre_save_post_receiver, sender=Products)





