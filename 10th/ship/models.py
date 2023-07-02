from django.db import models

class Shipment(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    expected_delivery_date = models.DateField()
    actual_delivery_date = models.DateField(blank=True, null=True)

class Cargo(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

class Tracking(models.Model):
    shipment = models.OneToOneField(Shipment, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('packing', 'Packing'),
        ('arrived_at', 'Arrived at'),
        ('dispatched_from', 'Dispatched from'),
        ('delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    location = models.CharField(max_length=100)
