from django.forms import ModelForm
from .models import Playlist


class CreatePlaylistForm(ModelForm):

    class Meta:
        model = Playlist
        fields = fields = [
            "list_title",
            "description",
            "image",
        ]