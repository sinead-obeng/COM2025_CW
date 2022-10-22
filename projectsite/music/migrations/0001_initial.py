# Generated by Django 3.2.15 on 2022-10-17 17:36

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
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=250)),
                ('genre', models.CharField(choices=[('afrobeats', 'AFROBEATS'), ('afrovibes', 'AFROVIBES'), ('alternative', 'ALTERNATIVE'), ('anime', 'ANIME'), ('bashment', 'BASHMENT'), ('blues', 'BLUES'), ("children's music", "CHILDREN'S MUSIC"), ('classical', 'CLASSICAL'), ('country', 'COUNTRY'), ('dance', 'DANCE'), ('dancehall', 'DANCEHALL'), ('electronic', 'ELECTRONIC'), ('hip-hop/rap', 'HIP-HOP/RAP'), ('holiday', 'H0LIDAY'), ('indie pop', 'INDIE POP'), ('jazz', 'JAZZ'), ('phonk', 'PHONK'), ('pop', 'POP'), ('r&b/soul', 'R&B/SOUL'), ('reggae', 'REGGAE'), ('rock', 'ROCK'), ('soundtrack', 'SOUNDTRACK')], default='genre', max_length=16)),
                ('song_title', models.CharField(max_length=250)),
                ('album_title', models.CharField(max_length=500)),
                ('is_favourite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_title', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('songs', models.ManyToManyField(to='music.Song')),
            ],
        ),
    ]
