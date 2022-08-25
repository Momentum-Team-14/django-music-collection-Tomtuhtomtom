from django.contrib import admin
from .models import Artist, Album, Genre, Cover

# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)

class CoverAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Cover, CoverAdmin)

# if I want to add list_display, fields, etc.
# class AlbumAdmin(admin.ModelAdmin):
#     pass


# class ArtistAdmin(admin.ModelAdmin):
#     pass