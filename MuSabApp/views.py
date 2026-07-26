from django.shortcuts import render
from .models import Album

# Create your views here.
def index(request):
    albums = Album.objects.all()

    return render(request, 'MuSabApp/index.html', {'title': 'Home', 'albums': albums})

def album_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'MuSabApp/album.html', {'title': album.album, 'album': album})

def timeline(request):
    albums = Album.objects.all().order_by('year')
    return render(request, 'MuSabApp/timeline.html', {'title': 'Timeline', 'albums': albums})

def discover(request):
    albums = Album.objects.all()
    return render(request, 'MuSabApp/discover.html', {'title': 'Discover', 'albums': albums})
