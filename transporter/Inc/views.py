

from django.contrib import messages
from django.shortcuts import render , redirect ,render_to_response
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
#from Inc.forms import FacultySignUpForm, LoginForm ,QuestionForm
from django.conf.urls import include, url
from django.urls import reverse
from django.db.models import Q
from Inc.models import User
from django.http import HttpResponseRedirect ,HttpResponse
#from Inc.models import QuestionPaper
from django.views import generic
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.template import RequestContext
'''

class FacultySignUpView(CreateView):
	model = User 
	form_class = FacultySignUpForm
	template_name = '/home/raju/django-apps/transporter/templates/registration/signup_form.html'

'''
'''
	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'faculty'
		return super().get_context_data(**kwargs)

	def form_valid(self , form):
		user = form.save()
		login(self.request, user)
		return redirect('Inc/home.html')
'''

'''
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()	
			return redirect('/Inc/')

			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username ,password=raw_password)
			login(request , user)
		
	else:
		form = SignUpForm()

	return render(request , 'Inc/signup.html',{'form' : form})

'''	

'''
def SolutionSubmission(request):
	answer = request.POST.get('option')
	#return render(request, "Inc/exam.html", {'answer':answer})


def DisplayAll(request):
	#q = QuestionPaper.objects.filter().values()
	form = QuestionPaper.objects.all()
	return render(request, 'Inc/exam.html/', {'form':form})


def NoOfQuestion(request):
	Q_number = request.POST.get('Q_number')
	return render(request ,'Inc/exam.html/' , {'Q_number':Q_number})

def Question(request):
	if request.method=='POST':
		form = QuestionPaper(request.POST)
		form.save()
		return render(request ,'Inc/exam.html/' , {'form':form})
	else:
		form = QuestionPaper()
		return render(request ,'Inc/exam.html/' , {'form':form})


def user_paper(request):
	form_class = QuestionForm()
	if request.method=='POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			picked = form.cleaned_data.get('picked')
			#do some thing with your results

	else:
		form = QuestionForm()
	return render_to_response('Inc/exam.html/', { 'form':form },RequestContext(request))

'''
'''
class QuestionPaper(CreateView):
	model = QuestionPaper
	template_name = 'Inc/exam.html'

	def get_queryset(self):
		questions = QuestionPaper.objects.all()
		return questions

'''		
'''

def Search(request):
	if request.method == 'POST':
		user = request.POST['srh']

		if user:
			user = User.objects.filter(Q(username__icontains=user) | Q(first_name__icontains=user))

			if user:
				return render(request, 'Inc/detail.html' , {'sr':user})
			else:
				messages.error(request, 'username DoesNotExist')

		else:
			return HttpResponseRedirect('')

	return render(request ,'Inc/detail.html/', messages.error(request , 'enter a valid user name.'))		

'''

'''
def my_view(request):
	username = request.POST['username']
	password = request.POST['password']
	use = authenticate(username=username,password=password)
	if user is not None:
		login(request, user)
		return redirect('/Inc/')
	else:
	
			return redirect('/Inc/login/')
'''			

'''

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = User.objects.filter(username=form.cleaned_data.get('username'))

			if user:
				username = form.cleaned_data.get('username')
				raw_password = form.cleaned_data.get('password')
				user = authenticate(username=username , password=raw_password)
				
				if user:	
					return redirect('/Inc/display')
			
				else:
					return render( request , '/Inc/login.html/' ,messages.error(request , 'invalid username/password.'))
					#messages.add_message(request , messages.INFO , 'invalid username/password.')
			else:
				print("user does not exit")     	
					
	else:
		form = LoginForm()
	return render(request, 'Inc/login.html' ,{'form' : form})

'''

def home(request):
	return render(request , 'Inc/home.html' )