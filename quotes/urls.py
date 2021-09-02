from django.urls import path
from . import views				#Jolo's, importing in the same folder

urlpatterns = [
	path('', views.home, name="home"),	#pertains to views.py in quotes
		#localhost:8000/

	path('about.html', views.about, name="about"),	#pertains to views.py in quotes
		#localhost:8000/about.html/

	path('add_stock.html', views.add_stock, name="add_stock"),

	path('delete/<stock_id>', views.delete, name="delete"),

	path('delete_stock.html', views.delete_stock, name="delete_stock"),
]
