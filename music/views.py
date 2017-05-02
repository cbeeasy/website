from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album


class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model= Album
    template_name='music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title','genre','album_logo']


#******************************************************************************************
'''from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    return render(request,'music/index.html', {'all_albums': all_albums})

def detail(request, album_id):
    album = get_object_or_404(Album, pk = album_id)
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk = album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album' : album,
            'error_message': "Attention vous n'avez pas choisi de chanson préférée !",
        })
    else:
        selected_song.is_favorite = not(selected_song.is_favorite)
        selected_song.save()
        #return render(request, 'music/detail.html', {'album': album})
        all_albums = Album.objects.all()
        return render(request, 'music/index.html', {'all_albums': all_albums})'''