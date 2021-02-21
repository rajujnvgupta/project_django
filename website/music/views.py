from django.views import generic
from django.views.generic.edit import CreateView , UpdateView ,DeleteView
from django.urls import reverse_lazy
from .models import Album
from django.shortcuts import render , redirect 
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .form import UserForm
class IndexView(generic.ListView):
	template_name = 'music/index.html'
	
	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html' 

class AlbumCreate(CreateView):
	model = Album
	fields = ['artist ' , 'album_title' ,'genre' ,'album_logo']

class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist ' , 'album_title' ,'genre' ,'album_logo']

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')

class UserFormView(View):
	from_class = UserForm
	template_name = 'music/registration_from.html'
	#display blank form
     def get(self , request):
     		form = self.form_class(None)
     		return render(request , self.template_name , {'form' : form})	
     		
     #process from data
     def POST(self , request):
     	form = self.form_class(request.POST)

     	if form.is_valid()		
				user = from.save(commit = False)
			#cleaned (normalised ) data
			username = from.cleaned_data['username']
			password = form.cleaned_data['password']
			user.save()

			# returns User objects if credintials are correct
			user = authenticate(username=username,password=password)
			 if user is not None:
			 	if user.is_active:
			 		login(request ,user)
			 		return redirect('music:index')
			 return render(request , self.template_name, {'form' : form})		

'''	
from django.http import Http404 #to restrict not showing not existing item on site
from django.http import HttpResponse
from django.template import loader  
from django.shortcuts import render ,get_object_or_404
from .models import Album, Song
# Create your views here.

def index(request):
	#return render(request ,'music/index.html' ,{'Album' : Album.objects.all()})
	all_album = Album.objects.all()
	#template = loader.get_template('template/music/index.html/')
	#passing Album information to dictionary
	context = {'all_album' : all_album }
	return render(request ,'music/index.html' ,context )
	#return HttpResponse(template.render(context))
#using template to separate backend from django	

	html = ''
	for album in all_album:
		url = '/music/' + str(album.id) + '/'
		html += '<a href = "' + url +'">' + album.album_title + '</a> <br>'
		return HttpResponse(html)
	
def detail(request , album_id):
	album = get_object_or_404(Album , pk = album_id)
	return render(request ,'music/detail.html' ,{'album' : album})
	#try:
	#	album = Album.objects.get(pk = album_id)
	#except Album.DoesNotExist:
	#	raise Http404(" Album does not existing")
	#return render(request ,'music/detail.html' ,{'album' : album})
	#return HttpResponse("<h1> album id is : "+ str(album_id) +"</h1>")


def favorite(request , album_id):
	album = get_object_or_404(Album , pk = album_id)
	try:
		select_song = album.song_set.get(pk = request.POST['song'])

	
	except (KeyError , Song.DoesNotExist):
		return render(request ,'music/detail.html' , {'album' : album , 'error_message' : "you did not select a valid song "})

	else: 
		select_song.is_favorite = True
		select_song.save()
		return render(request , 'music/detail.html' , {'album' : album})

'''