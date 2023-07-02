from django.shortcuts import render, get_object_or_404
from .models import Shipment, Cargo, Tracking

def shipment_detail_view(request, shipment_id):
    shipment = get_object_or_404(Shipment, pk=shipment_id)
    cargo = Cargo.objects.filter(shipment=shipment)
    tracking = Tracking.objects.filter(shipment=shipment)

    if request.method == 'POST':
        # Process form data for creating/updating cargo and tracking
        # Save the data to the database
        pass
    context = {
        'shipment': shipment,
        'cargo': cargo,
        'tracking': tracking,
    }

    return render(request, 'shipment_detail.html', context)

def shipment_delete_view(request, shipment_id):
    shipment = get_object_or_404(Shipment, pk=shipment_id)

    if request.method == 'POST':
        # Delete associated cargo and tracking
        cargo = Cargo.objects.filter(shipment=shipment)
        cargo.delete()

        tracking = Tracking.objects.filter(shipment=shipment)
        tracking.delete()

        # Delete the shipment
        shipment.delete()

        # Redirect to a success page or another view

    context = {
        'shipment': shipment,
    }

    return render(request, 'shipment_delete.html', context)
