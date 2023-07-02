from django.db import models

class Account(models.Model):
    account_number = models.CharField(max_length=10, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_type_choices = [
        ('Savings', 'Savings'),
        ('Credit', 'Credit'),
    ]
    account_type = models.CharField(max_length=10, choices=account_type_choices)

    def __str__(self):
        return f"Account {self.account_number}"
