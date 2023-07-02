from django.db import models
from .models import Product

class Product(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('appname.Product')

    def __str__(self):
        return self.name
