# practice

from django.shortcuts import render, redirect
from .models import Stock 				#, getting from models.py
from .forms import StockForm			#w/ line 44
from django.contrib import messages
# Create your views here.


def home(request):		#request= browser request
	import requests		#grabs stuff from the internet
	import json			#javascript notation; format for api

	if request.method == 'POST':
				# d POST is used to insert/update remote data.
		ticker = request.POST['ticker']
				# is name of the form action->input class->name in base.html
				# so if you search google, then ticker becomes google then sent back here.	
				

				#pk_6d45953d7d3745b0ab12ecf0613aa6c0 public keys
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_6d45953d7d3745b0ab12ecf0613aa6c0")		#url that connects to api
				#the data we get is being save in "api_request"

		try:
			api = json.loads(api_request.content)	#parse it in json, then save it in api
		except Exception as e:
			api = "Error..."
				#purpose of try and except, so that if there's a error
				#it would not malfunction and would only send "Error..."
		return render(request, 'home.html', {'api': api})	#in home.html

	else:
		return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})





def about(request):		#request= browser request
	return render(request, 'about.html', {})


def add_stock(request):		#request= browser request
	import requests		#grabs stuff from the internet
	import json			#javascript notation; format for api
	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been Added!"))
			return redirect('add_stock')

	else:
		ticker = Stock.objects.all()	
		output = []	
		for ticker_item in ticker:

			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_6d45953d7d3745b0ab12ecf0613aa6c0")		#url that connects to api
			#the data we get is being save in "api_request"

			try:
				api = json.loads(api_request.content)	#parse it in json, then save it in api
				output.append(api)
			except Exception as e:
				api = "Error..."	
										#this will show whats inside add stock in admin to our site
		return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})	#dictionary format 

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)	#pk is the i.d num
	item.delete()
	messages.success(request,("Stock has been deleted!"))
	return redirect(delete_stock)



def delete_stock(request):		#request= browser request
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker':ticker})