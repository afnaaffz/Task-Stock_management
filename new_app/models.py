from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_admin=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)


class CustomerRegister(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    dob = models.DateField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Stock(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    product = models.CharField(max_length=50)
    product_description = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()