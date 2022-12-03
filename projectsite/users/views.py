from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
    PasswordResetForm,
)


# Create your views here.
def forgot(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            messages.success(
                request,
                f"We've sent you an email containing a link that will allow you to reset your password. Once you receive the email follow the instructions to change your password.",
            )
            return redirect("forgot")
    else:
        form = PasswordResetForm()
    return render(request, "users/forgot.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            forename = form.cleaned_data["first_name"]
            surname = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "user_update_form": user_update_form,
        "profile_update_form": profile_update_form,
    }
    return render(request, "users/profile.html", context)
