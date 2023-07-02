from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    
    path('review_submit/', views.review_submit, name='review_submit'),
]
