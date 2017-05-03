from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def favorite(request, album_id):
    album = get_object_or_404(Album, pk = album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album' : album,
            'error_message': "Vous n'avez pas séléctionné une chanson !",
        })
    else:
        selected_song.is_favorite = not(selected_song.is_favorite)
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})

class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()
        #return an object_list for album in object_list...
        #context_object_name = 'all_albums' -> all_albums=object_list...

class DetailView(generic.DetailView):
    model= Album
    template_name='music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title','genre','album_logo']

    def get_context_data(self, **kwargs):
        context_data = super(AlbumCreate, self).get_context_data(**kwargs)
        context_data['page_title'] = 'Add a new album'
        return context_data

    #Rq On n'a pas besoin de lui donner le nom du template Django
    #va le chercher automatiquement (nom du model en minuscule _form.html dans template/music...)

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title','genre','album_logo']

    def get_context_data(self, **kwargs):
        context_data = super(AlbumUpdate, self).get_context_data(**kwargs)
        context_data['page_title'] = 'Edit an album'
        return context_data

class AlbumDelete(DeleteView):
    model=Album
    #where to go after delete ? -> index
    success_url = reverse_lazy('music:index')



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