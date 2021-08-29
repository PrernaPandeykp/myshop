from django.db import models
from django.contrib.auth.models import User
users = User.objects.values()


class Product(models.Model):
    product_id = models.AutoField
    product_name=models.CharField(max_length=30)
    category=models.CharField(max_length=50,default="")
    sub_category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=200)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="myapp/images",default="")

    def __str__(self):
        return self.product_name


class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    print(username,password)

