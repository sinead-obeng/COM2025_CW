from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, "blog/home.html")


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
            return redirect("blog-contact")
    else:
        form = ContactForm()
    return render(request, "blog/contact.html", {"form": form})
