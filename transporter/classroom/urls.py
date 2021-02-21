from django.conf.urls import url , include
from classroom import views 
from django.conf import settings
from classroom.view import faculty, classroom, students

app_name = 'classroom'
urlpatterns = [
	#url(r'^signup$' ,faculty.FacultySignUpView.as_view() , name='faculty_signup'),
	url(r'^$', views.test , name = 'class'),
]

