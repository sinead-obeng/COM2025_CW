from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

GENRE_CHOICES = (
    ("afrobeats", "AFROBEATS"),
    ("afrovibes", "AFROVIBES"),
    ("alternative", "ALTERNATIVE"),
    ("anime", "ANIME"),
    ("bashment", "BASHMENT"),
    ("blues", "BLUES"),
    ("children's music", "CHILDREN'S MUSIC"),
    ("classical", "CLASSICAL"),
    ("country", "COUNTRY"),
    ("dance", "DANCE"),
    ("dancehall", "DANCEHALL"),
    ("electronic", "ELECTRONIC"),
    ("hip-hop/rap", "HIP-HOP/RAP"),
    ("holiday", "H0LIDAY"),
    ("indie pop", "INDIE POP"),
    ("jazz", "JAZZ"),
    ("phonk", "PHONK"),
    ("pop", "POP"),
    ("r&b/soul", "R&B/SOUL"),
    ("reggae", "REGGAE"),
    ("rock", "ROCK"),
    ("soundtrack", "SOUNDTRACK"),
)


# Create your models here
class Song(models.Model):
    artist = models.CharField(max_length=250)
    genre = models.CharField(max_length=16, choices=GENRE_CHOICES, default="genre")
    song_title = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title


class Playlist(models.Model):
    User = settings.AUTH_USER_MODEL
    list_title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    songs = models.ManyToManyField(Song, blank=True)
    image = models.ImageField(
        default="placeholder-image.jpg", upload_to="playlist_pics"
    )

    def __str__(self):
        return self.list_title
