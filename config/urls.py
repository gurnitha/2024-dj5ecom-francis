# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # shop
    path("", include('app.shop.urls', namespace='shop')),

    # admin
    path("admin/", admin.site.urls),
]
