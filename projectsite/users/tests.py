from django.test import TestCase
from .models import Profile

# Create your tests here.
class TestCustomUser(TestCase):
    def setUp(self):
        Profile.objects.create()

    def test_profile_created(self):
        self.user = Profile.objects.create_user(username='testuser', password='12345', forename='Test', surname='User')
        login = self.client.login(username='testuser', password='12345')