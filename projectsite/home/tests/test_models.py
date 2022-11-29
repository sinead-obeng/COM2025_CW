from django.test import TestCase
from home.models import Contact, Post


# Create your tests here.
class HomeModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        c1 = Contact(email="tester1@email.com", subject="My first test.", message="This is my first message.")
        c1.save()
        c2 = Contact(email="tester2@email.com", subject="My second test.", message="This is my second message.")
        c2.save()
        c3 = Contact(email="tester3@email.com", subject="My third test.", message="This is my third message.")
        c3.save()

    def test_setup_data(self):
        self.assertEquals(3, Contact.objects.all().count())
