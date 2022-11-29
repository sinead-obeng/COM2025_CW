from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Post
from .forms import ContactForm


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "home/home.html", context)


def about(request):
    return render(request, "home/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            messages.success(
                request,
                "Thank you for your inquiry! Your contact information and message was successfully submitted.",
            )
            return redirect("home-contact")
    else:
        form = ContactForm()
    return render(request, "home/contact.html", {"form": form})
