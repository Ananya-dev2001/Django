from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns

    path('create_or_update_account/', views.create_or_update_account, name='create_or_update_account'),
]
