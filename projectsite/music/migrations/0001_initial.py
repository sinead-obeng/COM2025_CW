# Generated by Django 3.2.15 on 2022-11-06 00:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("artist", models.CharField(max_length=250)),
                ("playlist", models.CharField(max_length=500)),
                (
                    "genre",
                    models.CharField(
                        choices=[
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
                        ],
                        default="genre",
                        max_length=16,
                    ),
                ),
                ("song_title", models.CharField(max_length=250)),
                ("album_title", models.CharField(max_length=500)),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                ("duration", models.DurationField(default=datetime.timedelta)),
                ("is_favourite", models.BooleanField(default=False)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Playlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("list_title", models.CharField(max_length=500)),
                ("description", models.TextField(blank=True)),
                (
                    "date_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "image",
                    models.ImageField(
                        default="placeholder-image.jpg", upload_to="playlist_pics"
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
