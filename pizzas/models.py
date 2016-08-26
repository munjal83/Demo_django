from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pizza(models.Model):
	"""The name of the Pizza"""
	name = models.CharField(max_length=50)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""String representation of the name"""
		return self.name
		
class Topping(models.Model):
	"""Name of the toppings"""
	pizza = models.ForeignKey(Pizza)
	name = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		"""String representation of the names"""
		return self.name