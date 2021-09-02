from django import forms
from .models import Stock 

class StockForm(forms.ModelForm):	#forms from django, then inside we want ModelForm
	class Meta: #inner class of your model class, 
				# used to change the behavior of your model fields like changing order options,
				#verbose_name and lot of other options.
		model = Stock
		fields = ["ticker"]
		#Variables that belong to an object
		# or class are referred to as fields
