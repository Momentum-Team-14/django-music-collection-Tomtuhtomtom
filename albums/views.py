from django.shortcuts import render
from .models import Album, Artist
from django.views import generic

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


class AlbumDetailView(generic.DetailView):
    model = Album
