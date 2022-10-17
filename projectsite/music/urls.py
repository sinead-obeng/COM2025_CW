from django.urls import path
from . import views

urlpatterns = [
    path('playlist/', views.playlist, name='music-playlist'),
]