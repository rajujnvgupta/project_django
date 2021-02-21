from django.shortcuts import render
from django.views.generic.dates import YearArchiveView

from webtech.models import Article
# Create your views here.
class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    #by default it is false
    make_object_list = True
    allow_future = True
    template_name_suffix = 'templates/article_archive.html'

def home(request):
	return render(request,'webtech/home.html')