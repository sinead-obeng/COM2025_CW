from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "my-class",
                "placeholder": "Email",
            }
        ),
        required=True,
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "my-class",
                "placeholder": "Subject",
            }
        ),
        required=True,
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"style": "width: 100%; resize:none;"}),
        required=True,
    )

    class Meta:
        model = Contact
        fields = '__all__'