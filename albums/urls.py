from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums/', views.AlbumListView.as_view(), name='albums'),
    path('album/<int:pk>', views.AlbumDetailView.as_view(), name='album-detail'),
    path('artists/', views.ArtistListView.as_view(), name='artists'),
    path('artist/<int:pk>', views.ArtistDetailView.as_view(), name='artist-detail'),
]

urlpatterns += [
    path('artist/create/', views.ArtistCreate.as_view(), name='artist-create'),
    path('artist/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artist-update'),
    path('artist/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artist-delete'),
]

urlpatterns += [
    path('album/create/', views.AlbumCreate.as_view(), name='album-create'),
    path('album/<int:pk>/update/', views.AlbumUpdate.as_view(), name='album-update'),
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
]
