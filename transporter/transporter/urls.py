"""transporter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from django.conf.urls import include,url
from Inc import views
#from rest_framework.urlpatterns import format_suffic_patterns

#admin.site.site_header = 'Custom Admin'
#admin.site.site_title = 'Custom Admin'
#admin.site.site_url = 'http://custom.com'
#admin.site.index_title = 'Custom administration index'

urlpatterns = [
	
    url('^classroom/', include('classroom.urls', namespace='classroom')),
 	url('^Inc/' , include('Inc.urls', namespace='Inc')), 
    url('accounts', include('django.contrib.auth.urls')),
    url('^admin/', admin.site.urls),
   # url('^accouts/signup/faculty/' , views.FacultySignUpView.as_view(), name='faculty_signup'),
 ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

