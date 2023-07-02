from django.shortcuts import render, redirect
from .forms import ShipmentForm

def create_shipment_view(request):
    form = ShipmentForm()

    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shipment_list')

    context = {
        'form': form,
    }

    return render(request, 'create_shipment.html', context)

from django.shortcuts import render, redirect
from .models import Shipment

def delete_shipment_view(request, shipment_id):
    shipment = Shipment.objects.get(pk=shipment_id)

    if request.method == 'POST':
        shipment.delete()
        return redirect('shipment_list')

    context = {
        'shipment': shipment,
    }

    return render(request, 'delete_shipment.html', context)

from django.shortcuts import render
from .models import Shipment

def shipment_list_view(request):
    shipments = Shipment.objects.all()

    for shipment in shipments:
        if shipment.actual_delivery_date:
            if shipment.actual_delivery_date > shipment.expected_delivery_date:
                shipment.status = 'delayed'
            elif shipment.actual_delivery_date < shipment.expected_delivery_date:
                shipment.status = 'early'
            else:
                shipment.status = 'on-time'

    context = {
        'shipments': shipments,
    }

    return render(request, 'shipment_list.html', context)
