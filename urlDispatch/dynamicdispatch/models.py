from django.db import models

# Create your models here.

class Books(models.Model):
	book_name = models.CharField(max_length=225, primary_key=True)
	authon = models.CharField(max_length=100)
	def __str__(self):
		return self.book_name