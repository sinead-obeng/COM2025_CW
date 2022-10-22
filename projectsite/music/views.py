from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


from .forms import CreatePlaylistForm
from .models import Playlist


# Create your views here.
def playlist(request):
    context = {
        'playlists': Playlist.objects.all(),
        'user': User.objects.get(username=request.user),
    }
    return render(request, "music/playlist.html", context)


def create_playlist(request):
    if request.method == "POST":

        ins = Playlist(
            list_title=request.POST['list_title'],
            description=request.POST['description'],
            creator=request.user,
            image=request.POST['image']
        )
        ins.save()
        messages.success(
            request,
            f"Playlist '{request.POST['list_title']}' created!",
        )
        return redirect("music-playlist")
    else:
        form = CreatePlaylistForm()
    return render(request, "music/addplaylist.html", {'form': form})
