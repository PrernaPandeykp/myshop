from django.db import models
from django.contrib.auth.models import User

users = User.objects.values()


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=10, default="")
    master_category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    article_type = models.TextField(max_length=150, default="")
    base_colour = models.CharField(max_length=50, default="")
    season = models.CharField(max_length=50, default="")
    year = models.IntegerField(default=0)
    usage = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=300, default="")
    price = models.CharField(max_length=200)
    discount_price = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=50, default="")
    age_group = models.CharField(max_length=50, default="")


class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    print(username, password)
