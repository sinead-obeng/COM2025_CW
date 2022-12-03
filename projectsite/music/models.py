from datetime import timedelta

from django.core.validators import MinValueValidator
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils import timezone
from PIL import Image

GENRE_CHOICES = [
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
]


# Create your models here
class Playlist(models.Model):
    User = settings.AUTH_USER_MODEL
    list_title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(
        default="placeholder-image.png", upload_to="playlist_pics/"
    )

    def __str__(self):
        return self.list_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse(
            "music-display_playlist",
            kwargs={"pk": Playlist.objects.get(pk=self.kwargs.get("pk")).pk},
        )


class Song(models.Model):
    User = settings.AUTH_USER_MODEL
    artist = models.CharField(max_length=250)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist = models.CharField(max_length=500)
    genre = models.CharField(max_length=16, choices=GENRE_CHOICES, default="genre")
    song_title = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    date_added = models.DateTimeField(default=timezone.now)
    duration = models.DurationField(default=timedelta)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title


class Favourites(models.Model):
    song_title = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_title
