from django import forms
from django.forms import ModelForm
from .models import Playlist, Song
from django.conf import settings

GENRE_CHOICES = (
    ("afrobeats", "Afrobeats"),
    ("afrovibes", "Afrovibes"),
    ("alternative", "Alternative"),
    ("anime", "Anime"),
    ("bashment", "Bashment"),
    ("blues", "Blues"),
    ("children's music", "Children's music"),
    ("classical", "Classical"),
    ("country", "Country"),
    ("dance", "Dance"),
    ("dancehall", "Dancehall"),
    ("electronic", "Electronic"),
    ("hip-hop/rap", "Hip-hop/Rap"),
    ("holiday", "Holiday"),
    ("indie pop", "Indie pop"),
    ("jazz", "Jazz"),
    ("phonk", "Phonk"),
    ("pop", "Pop"),
    ("r&b/soul", "R&B/Soul"),
    ("reggae", "Reggae"),
    ("rock", "Rock"),
    ("soundtrack", "Soundtrack"),
)


class CreatePlaylistForm(ModelForm):
    list_title = forms.CharField(label="Name", max_length=500)
    description = forms.CharField(
        label="Description (add an optional description)",
        widget=forms.Textarea(attrs={"style": "width: 100%; resize:none;"}),
        required=False,
    )
    image = forms.ImageField(required=False)

    class Meta:
        model = Playlist
        fields = [
            "list_title",
            "description",
            "image",
        ]
        exclude = ("creator",)


class AddSongForm(ModelForm):
    artist = forms.CharField(max_length=250)
    genre = forms.CharField(widget=forms.Select(choices=GENRE_CHOICES))
    song_title = forms.CharField(max_length=250)
    album_title = forms.CharField(max_length=500)
    is_favourite = forms.BooleanField()

    class Meta:
        model = Song
        fields = ["artist", "genre", "song_title", "album_title", "is_favourite"]

    field_order = ["song_title", "artist"]
