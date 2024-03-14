# app/shop/views.py

# Django dan third party modules
from django.shortcuts import render

# Locals
from app.shop.models import Slider 

# Create your views here.

def home_view(request):
	sliders = Slider.objects.all()
	print(sliders)
	data = {
		'sliders':sliders,
	}
	return render(request, 'shop/index.html', data)