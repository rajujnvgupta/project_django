from django.shortcuts import render
from .models import Books
# Create your views here.

def index(request):
	obj = Books.objects.all()
	return	render(request, 'dynamicdispatch/index.html', {'obj':obj})

def details(request, pk):
	

