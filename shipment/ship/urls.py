from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_shipment_view, name='create_shipment_view'),
    path('delete/<int:shipment_id>/', views.delete_shipment_view, name='delete_shipment_view'),
    path('list/', views.shipment_list_view, name='shipment_list'),
]
