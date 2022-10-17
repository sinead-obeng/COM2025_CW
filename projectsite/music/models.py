from django.db import models

GENRE_CHOICES = (
    ("afrobeats", "AFROBEATS"),
    ("afrovibes", "AFROVIBES"),
    ("alternative","ALTERNATIVE"),
    ("anime", "ANIME"),
    ("bashment", "BASHMENT"),
    ("blues","BLUES"),
    ("children's music","CHILDREN'S MUSIC"),
    ("classical","CLASSICAL"),
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


# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=16, choices=GENRE_CHOICES, default='genre')
    album_photo = models.ImageField(default='placeholder-image.png', upload_to='album_pics')

    def __str__(self):
        return f"{self.album_title} - {self.artist}"




class Song(models.Model):
    album = models.ForeignKey(Album)
    song_title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
