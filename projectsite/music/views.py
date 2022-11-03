from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.generic import DetailView


from .forms import CreatePlaylistForm
from .models import Playlist
from blog.models import Post


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
        ins2 = Post(
            title="New playlist created.",
            content=f"You created a playlist called {request.POST['list_title']}.",
            date_posted=timezone.now(),
            author=request.user
        )
        ins2.save()
        messages.success(
            request,
            f"Playlist '{request.POST['list_title']}' created!",
        )
        return redirect("music-playlist")
    else:
        form = CreatePlaylistForm()
    return render(request, "music/addplaylist.html", {'form': form})


class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'music/displayplaylist.html'



def add_song(request):
    context = {
        'playlists': Playlist.objects.all(),
    }
    return render(request, 'music/addsong.html', context)
