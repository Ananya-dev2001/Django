from django.db import models

class Customer(models.Model):
    accounts = models.ManyToManyField(Account)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
