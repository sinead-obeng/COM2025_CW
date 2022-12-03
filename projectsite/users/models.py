from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(
        max_length=255, default="default", validators=[ASCIIUsernameValidator]
    )
    forename = models.CharField(max_length=100, default="default")
    surname = models.CharField(max_length=100, default="default")
    email = models.EmailField(default="default@email.com")
    image = models.ImageField(default="default.jpg", upload_to="profile_pics/")

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
