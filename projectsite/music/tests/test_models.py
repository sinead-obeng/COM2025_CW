from django.contrib.auth.models import User
from music.models import Playlist
from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.
class MusicModelTests(TestCase):
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
        p2 = Playlist(
            list_title="Test Playlist2",
            description="This is my second test playlist.",
            creator=u1,
            image="placeholder-image.png",
        )
        p2.save()
        p3 = Playlist(
            list_title="Test Playlist3",
            description="This is my third test playlist.",
            creator=u1,
            image="placeholder-image.png",
        )
        p3.save()

    def test_setup_data(self):
        self.assertEquals(3, Playlist.objects.all().count())
