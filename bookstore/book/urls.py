from django.urls import path
from . import views

urlpatterns = [
    path('bookstore/', views.bookstore, name='bookstore'),
]
