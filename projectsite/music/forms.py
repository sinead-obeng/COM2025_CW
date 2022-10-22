from django import forms
from django.forms import ModelForm
from .models import Playlist


class CreatePlaylistForm(ModelForm):
    list_title = forms.CharField(label="Name", max_length=500)
    description = forms.CharField(
        label="Description (add an optional description)",
        widget=forms.Textarea(attrs={"style": "width: 100%; resize:none;"}),
        required=False,
    )
    image = forms.ImageField(required=False)

    class Meta:
        model = Playlist
        fields = [
            "list_title",
            "description",
            "image",
        ]
