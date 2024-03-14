# app/shop/models.py

# Django and third party modules
from django.db import models

# Create your models here.

class Slider(models.Model):
	title 		= models.CharField(max_length=60, blank=False, null=False)
	description = models.CharField(max_length=120, blank=False, null=False)
	button_text = models.CharField(max_length=60, blank=False, null=False)
	button_link = models.CharField(max_length=255, blank=False, null=False)
	image 		= models.ImageField(upload_to="sliders/%Y/%m/%d/", blank=False, null=False)
	created_at 	= models.DateTimeField(auto_now_add=True)
	updated_at 	= models.DateTimeField(auto_now=True)