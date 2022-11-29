from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.
class HomeViewTests(TestCase):

    @classmethod
    def setUp(self):
        return

    def test_home_page_loads(self):
        client = Client()

        response = client.get(reverse('home-home'))

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, '<h1>Welcome</h1>')

    def test_about_page_loads(self):
        client = Client()

        response = client.get(reverse('home-about'))

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, '<h1>About</h1>')

    def test_contact_page_loads(self):
        client = Client()

        response = client.get(reverse('home-contact'))

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, '<h1>Contact Us</h1>')
