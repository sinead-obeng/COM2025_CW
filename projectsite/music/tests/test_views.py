from django.contrib.auth.models import User
from music.models import Playlist
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime


# Create your tests here.
class MusicViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        u1 = User.objects.create_user(username="testuser1", password="12345")
        u1.save()
        p1 = Playlist(
            list_title="Test Playlist1",
            description="This is my first test playlist.",
            creator=u1,
            image="placeholder-image.png",
        )
        p1.save()

    def test_playlist_page_loads(self):
        client = Client()
        client.login(username="testuser1", password="12345")

        response = client.get(reverse("music-playlist"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "<h1>My Playlists</h1>")

    def test_create_playlist_page_loads(self):
        client = Client()

        response = client.get(reverse("music-create_playlist"))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "<h1>Create playlist</h1>")

    def test_display_playlist_page_loads(self):
        client = Client()

        response = client.get(reverse("music-display_playlist", kwargs={"pk": 1}))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "<h1>Test Playlist1</h1>")

    def test_add_song_page_loads(self):
        client = Client()

        response = client.get(reverse("music-add_song", kwargs={"pk": 1}))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "<h1>Add Song</h1>")
