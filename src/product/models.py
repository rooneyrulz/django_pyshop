from django.conf import settings
from django.urls import reverse
from django.db import models

class Product(models.Model):
	provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=10000, decimal_places=2)
	description = models.TextField(default="It's newest product", blank=True)
	date = models.DateTimeField(auto_now_add=True)
	is_local = models.BooleanField(default=True)


	def __str__(self):
		return self.name


	def get_absolute_url(self):
		return reverse('product:product_details_view', kwargs={'id': self.id})
