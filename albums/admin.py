from django.contrib import admin
from .models import Artist, Album

# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)


# if I want to add list_display, fields, etc.
# class AlbumAdmin(admin.ModelAdmin):
#     pass


# class ArtistAdmin(admin.ModelAdmin):
#     pass