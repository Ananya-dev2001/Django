from django import forms
from .models import Shipment

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['origin', 'destination', 'expected_delivery_date', 'actual_delivery_date']
