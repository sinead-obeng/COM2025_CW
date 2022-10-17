from django.shortcuts import render

from .forms import CreatePlaylistForm


# Create your views here.
def playlist(request):
    return render(request, "music/playlist.html")


def create_playlist(request):
    form = CreatePlaylistForm()
    return render(request, "music/addplaylist.html", {'form': form})