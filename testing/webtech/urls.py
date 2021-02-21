from django.conf.urls import url , include
from django.conf import settings
from django.views.generic.dates import ArchiveIndexView
from webtech.views import ArticleYearArchiveView
from webtech.models import Article
from . import views
app_name = 'webtech'

urlpatterns = [
	url(r'^archive/$',ArchiveIndexView.as_view(model=Article,date_field="pub_date"),name='article_archive'),
	url(r'^(?P<year>[0-9]{4})/$',ArticleYearArchiveView.as_view(),name="article_year_archive"),
	url(r'^$', views.home , name='home'),
]