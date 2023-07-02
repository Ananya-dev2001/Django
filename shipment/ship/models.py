from django.db import models

class Shipment(models.Model):
    STATUS_CHOICES = (
        ('early', 'Early'),
        ('on-time', 'On Time'),
        ('delayed', 'Delayed'),
        ('en-route', 'En Route'),
    )

    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    expected_delivery_date = models.DateField()
    actual_delivery_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en-route')

    def __str__(self):
        return f"Shipment from {self.origin} to {self.destination}"
