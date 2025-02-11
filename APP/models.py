from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    URL_image = models.CharField(max_length=255)

    class Meta:
        db_table = 'APP_album'  # specify the table name here

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    URL_image = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    fileName = models.CharField(max_length=255)
    URL_music = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')

    class Meta:
        db_table = 'APP_songs'  # specify the table name here

    def __str__(self):
        return self.name