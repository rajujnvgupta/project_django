from django.contrib import admin
from .models import Album , Song
#album class has admin interface
# Register your models here.

admin.site.register(Album)
admin.site.register(Song)