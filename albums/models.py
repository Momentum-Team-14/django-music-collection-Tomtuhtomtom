from django.db import models
from django.urls import reverse


class Album(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a album')
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('album-detail-view', args=[str(self.id)])


class Artist(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a band or artist')
    
    def get_absolute_url(self):
        return reverse('artist-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name