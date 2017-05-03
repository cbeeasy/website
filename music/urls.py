from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
    #On a défini des views generic url demande des fonctions donc on utilise
    #as_view pour transformer la class en view exploitable par url
    #rq pk pour récupérer la clé primaire...

    # Create /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), {'page_title':'Add a new album'},name='album-add'),
    # pas de pk puisque add...

    # Update /music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # Delete /music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/<album_id>/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]

