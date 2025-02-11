from rest_framework import serializers
from .models import Song, Album


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['name', 'image', 'artist', 'fileName', 'URL_image', 'URL_music']


class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = Album
        fields = ['name', 'image', 'songs', 'URL_image']
