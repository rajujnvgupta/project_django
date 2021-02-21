
from django.conf.urls import url , include
from Inc import views , forms
from django.conf import settings

#from .views import QuestionPaper

app_name ='Inc'

urlpatterns = [
	
	 url(r'^$' ,views.home, name = 'home'),
	 #url(r'^register-medical/$' , views.signup, name = 'register-medical'),
	 #url(r'^register-jee/$' , views.signup, name = 'register-jee'),
   #url(r'^$' , views.home, name = 'logout'),
   #url(r'^login$' ,views.login ,name = 'login'),
   #url(r'^search$' , views.Search , name = 'search'),

  #only for admin
  # url(r'^user_answer$' ,views.user_paper ,name = 'user_answer'),
   #url(r'^Q_number$', views.QuestionPaper.as_view() ,name = 'Q_number'),
   #url(r'^question$' ,views.Question.as_view() , name = 'question'),
    #url(r'^question$' ,views.Question , name = 'question'),
    #url(r'^display$' ,views.DisplayAll , name = 'display'),
    #url(r'^display$', views.SolutionSubmission, name = 'display'),
   #url(r'^search$' , views.Search , name = 'search'),
   	#url(r'^login/$', views.login, {'template_name': 'Inc/login.html'}, name='login'),

]