from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums/', views.AlbumListView.as_view(), name='albums'),
    path('album/<int:pk>', views.AlbumDetailView.as_view(), name='album-detail'),
    path('artists/', views.ArtistListView.as_view(), name='artists'),
    path('artist/<int:pk>', views.ArtistDetailView.as_view(), name='artist-detail'),
]
