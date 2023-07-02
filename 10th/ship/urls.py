from django.urls import path
from . import views

app_name = 'ship'

urlpatterns = [
    path('shipment/<int:shipment_id>/', views.shipment_detail_view, name='shipment_detail'),
    path('shipment/<int:shipment_id>/delete/', views.shipment_delete_view, name='shipment_delete'),
    # Other URL patterns
]
