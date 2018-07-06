from django.db import models

# Create your models here.
class Product(models.Model):
    # name = models.CharField(max_length = 250),
    imglink = models.CharField(max_length = 800, default="0000000")
    name = models.CharField(max_length = 500, default="0000000")
    description = models.TextField(default="0000000")
    price = models.FloatField(default="0000000")


class Order(models.Model):
    fulfilled = models.BooleanField(default = False)
    items = models.TextField(default="0000000")
    first_name = models.CharField(max_length = 400, default="0000000")
    last_name = models.CharField(max_length = 400, default="0000000")
    address = models.CharField(max_length = 400, default="0000000")
    city = models.CharField(max_length = 400, default="0000000")
    payment_method = models.CharField(max_length = 400, default="0000000")
    payment_data = models.CharField(max_length = 400, default="0000000")