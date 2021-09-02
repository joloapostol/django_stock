from django.contrib import admin
from .models import Stock   	
	#JOLO's, it is stock because we're importing CLASS stock
	# in models.py

admin.site.register(Stock)
# Register your models here.
