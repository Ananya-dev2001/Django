from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Other URL patterns
    path('shipments/', include('ship.urls')),
]
