from django.core import mail
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

    def test_send_email(self):
        mail.send_mail('Test subject here', 'Here is the test message.',
                       'from.testuser1@email.com', ['to@example.com'],
                       fail_silently=False)

        self.assertEqual(1, len(mail.outbox))
        self.assertEqual(mail.outbox[0].subject, 'Test subject here')
