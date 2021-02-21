from django.db import models

# Create your models here.
from django.urls import reverse

class Article(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateField()

	def get_absolute_url(self):
		return reverse('article-detail', kwargs={'pk':self.pk})