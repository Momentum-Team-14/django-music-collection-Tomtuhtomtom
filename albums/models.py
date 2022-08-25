from django.db import models
from django.urls import reverse


class Album(models.Model):
    cover = models.ForeignKey('Cover', on_delete=models.SET_NULL, related_name='albums', blank=True, null=True)
    title = models.CharField(max_length=200, help_text='Enter an album')
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, related_name='albums', blank=True, null=True)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, related_name='albums', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('album-detail', args=[str(self.id)])


class Artist(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a band or artist')
    
    def get_absolute_url(self):
        return reverse('artist-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a music genre')

    def __str__(self):
        return self.name


class Cover(models.Model):
    image = models.ImageField(upload_to="media")
    title = models.CharField(max_length=200, help_text='Enter a title for this image')

    def __str__(self):
        return self.title
