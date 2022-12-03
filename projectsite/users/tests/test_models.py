from django.contrib.auth.models import User
from django.test import TestCase
from users.models import Profile


# Create your tests here.
class UserModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        u1 = User.objects.create_user(username="testuser1", password="12345")
        u1.save()
        u2 = User.objects.create_user(username="testuser2", password="12345")
        u2.save()
        u3 = User.objects.create_user(username="testuser3", password="12345")
        u3.save()

    def test_setup_data(self):
        self.assertEquals(3, User.objects.all().count())
        self.assertEquals(3, Profile.objects.all().count())
