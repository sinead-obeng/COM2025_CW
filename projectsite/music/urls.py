from django.urls import path

from . import views
from .views import PlaylistDetailView

urlpatterns = [
    path('playlist/', views.playlist, name='music-playlist'),
    path('create_playlist/', views.create_playlist, name='music-create_playlist'),
    path('/<int:pk>/', PlaylistDetailView.as_view(), name='music-display_playlist'),
    path('add_song', views.add_song, name='music-add_song')
]