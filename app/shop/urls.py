# app/shop/urls.py

# Django dan third party modules
from django.urls import path

# Locals
from app.shop.views import home_view

# namespace
app_name = "shop"

# urls patterns
urlpatterns = [
    path("", home_view, name="home"),
]
