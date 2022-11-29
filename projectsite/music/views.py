from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.views.generic import CreateView, DetailView


from .forms import CreatePlaylistForm, AddSongForm
from .models import Playlist, Song
from home.models import Post


# Create your views here.
def playlist(request):
    context = {
        "playlists": Playlist.objects.all(),
        "user": User.objects.get(username=request.user),
    }
    return render(request, "music/playlist.html", context)


def create_playlist(request):
    if request.method == "POST":
        image = request.POST["image"]
        if image == "":
            image = "placeholder-image.png"
        ins = Playlist(
            list_title=request.POST["list_title"],
            description=request.POST["description"],
            creator=request.user,
            image="playlist_pics/" + image,
        )
        ins.save()
        ins2 = Post(
            title="New playlist created.",
            content=f"You created a playlist called {request.POST['list_title']}.",
            date_posted=timezone.now(),
            author=request.user,
        )
        ins2.save()
        messages.success(
            request,
            f"Playlist '{request.POST['list_title']}' created!",
        )
        return redirect("music-playlist")
    else:
        form = CreatePlaylistForm()
    return render(request, "music/addplaylist.html", {"form": form})


class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = "music/displayplaylist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["songs"] = Song.objects.filter(playlist=Playlist.objects.get(pk=self.kwargs.get("pk")).list_title)
        return context


class SongAddView(CreateView):
    model = Song
    template_name = "music/addsong.html"
    fields = [
        "artist",
        "genre",
        "song_title",
        "album_title",
        "duration",
        "is_favourite",
    ]

    def form_valid(self, form):
        form.instance.playlist = Playlist.objects.get(
            pk=self.kwargs.get("pk")
        ).list_title
        form.instance.creator = Playlist.objects.get(pk=self.kwargs.get("pk")).creator
        ins = Post(
            title="New song added to playlist.",
            content=f"You added {form.instance.song_title} to your {form.instance.playlist} playlist.",
            date_posted=timezone.now(),
            author=form.instance.creator,
        )
        ins.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "music-display_playlist",
            kwargs={"pk": Playlist.objects.get(pk=self.kwargs.get("pk")).pk},
        )
