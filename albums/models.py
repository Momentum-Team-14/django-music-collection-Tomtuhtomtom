from django.db import models
from django.urls import reverse


class Album(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a album')
    artist = models.ManyToManyField('Artist', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-title', '-artist', '-created_at']

    def get_absolute_url(self):
        return reverse('album-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a artist')
    album = models.ManyToManyField('Album', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-name', '-album']

    def get_absolute_url(self):
        return reverse('artist-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name