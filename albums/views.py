from django.shortcuts import render
from .models import Album, Artist, Genre, Cover
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from albums.models import Artist
from django.http import Http404


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_albums = Album.objects.all().count()

    # The 'all()' is implied by default.
    num_artists = Artist.objects.count()

    context = {
        'num_albums': num_albums,
        'num_artists': num_artists,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class AlbumListView(generic.ListView):
    model = Album
    paginate_by = 10


class AlbumDetailView(generic.DetailView):
    model = Album


class ArtistListView(generic.ListView):
    model = Artist
    paginate_by = 10


class ArtistDetailView(generic.DetailView):
    model = Artist

class ArtistCreate(CreateView):
    model = Artist
    fields = ['name']

class ArtistUpdate(UpdateView):
    model = Artist
    fields = '__all__' # Not recommended (potential security issue if more fields added)

class ArtistDelete(DeleteView):
    model = Artist
    success_url = reverse_lazy('artists')

class AlbumCreate(CreateView):
    model = Album
    fields = ['cover', 'title', 'artist', 'genre']

class AlbumUpdate(UpdateView):
    model = Album
    fields = '__all__' # Not recommended (potential security issue if more fields added)

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('albums')


def image(request, cover_id):
    Cover.objects.get(pk=cover_id)
    if image is not None:
        return render(request, 'images/image.html', {'image': image})
    else:
        raise Http404('Image does not exist')
