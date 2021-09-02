from django.db import models #this models

# Create your models here.

class Stock(models.Model): #Importing that from top to models
	ticker = models.CharField(max_length=10) #CharField is a database datatype, Character

	def __str__(self):
		return self.ticker	#this is for the admin area