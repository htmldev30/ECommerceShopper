# Generated by Django 3.0.6 on 2020-06-09 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_bio', models.CharField(max_length=50)),
                ('user_pic', models.ImageField(upload_to='user_image')),
                ('user_background', models.ImageField(upload_to='user_image_back')),
                ('product', models.ManyToManyField(blank=True, to='Products.Products')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]