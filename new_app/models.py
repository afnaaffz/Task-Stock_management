from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_admin=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)


class CustomerRegister(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)


class Stock(models.Model):
    name = models.CharField(max_length=20)
    stock_id = models.IntegerField()
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()