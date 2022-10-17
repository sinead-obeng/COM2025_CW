from django.shortcuts import render


# Create your views here.
def playlist(request):
    return render(request, "music/playlist.html")
