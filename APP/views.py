from django.http import JsonResponse
from .models import Song
from .serializers import AlbumSerializer, SongSerializer


def get_song(request):
    songs = Song.objects.select_related('album').all()
    albums = {}

    for song in songs:
        album_name = song.album.name
        album_image = song.album.image
        album_url_image = song.album.URL_image

        if album_name not in albums:
            albums[album_name] = {'name': album_name, 'image': album_image, 'URL_image': album_url_image, 'songs': []}

        albums[album_name]['songs'].append(SongSerializer(song).data)

    serializer = AlbumSerializer(albums.values(), many=True)
    return JsonResponse(serializer.data, safe=False)
