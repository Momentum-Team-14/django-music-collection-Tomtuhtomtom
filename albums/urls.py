from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums/', views.AlbumListView.as_view(), name='albums'),
    path('album/<int:pk>', views.AlbumDetailView.as_view(), name='album-detail'),
]
