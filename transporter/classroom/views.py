from django.shortcuts import render ,redirect

# Create your views here.
def test(request):
	return render(request ,'classroom/home.html')