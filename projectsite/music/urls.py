from django.urls import path
from . import views

urlpatterns = [
    path('playlist/', views.playlist, name='music-playlist'),
    path('create_playlist/', views.create_playlist, name='music-create_playlist')
]