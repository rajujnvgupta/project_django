from django.conf.urls import url
from django.conf import settings
from . import views
#from django.conf.urls.static import static

app_name = 'music'

urlpatterns = [

	
	#/music/
	url(r'^$' , views.IndexView.as_view() , name = 'index'),
	#register
	url(r'^register/$' , views.UserFormView.as_view() , name = 'register'),
	url(r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view() , name ='detail'),
	#/music/album/add/
	url(r'album/add/$' , views.AlbumCreate.as_view() , name = 'album-add'),
	#/music/album/2/
	url(r'^album/(?P<pk>[0-9]+)/$' , views.AlbumUpdate.as_view() , name ='album-update'),
	#/music/album/2/delete/
	url(r'^album/(?P<pk>[0-9]+)/delete/$' , views.AlbumDelete.as_view() , name ='album-delete'),
	#url(r'^$' , views.index , name = 'index'),

	#url('^music/', include('music.urls', namespace='music')
   # path('admin/', admin.site.urls),

    #music/album_id/
    #url(r'^(?p<album_id>[0-9]+)/$' , views.detail , name ='detail'), not working why
    #url(r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view() , name ='detail'),
    #url(r'^(?P<album_id>[0-9]+)/$' , views.detail , name ='detail'),
    #url(r'^$' , views.detail , name ='detail'),

   # url(r'^(?P<album_id>[0-9]+)/favorite/$' , views.favorite , name ='favorite'),


] # + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)