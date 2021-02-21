from django.db import models
from django.urls import reverse

class Article(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateField()

	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse('article-detail', kwargs={'pk':self.pk})