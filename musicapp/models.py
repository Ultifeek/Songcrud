from pickle import TRUE
from django.db import models
from datetime import datetime

# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    age = models.IntegerField()


    def __str__(self):
        return self.first_name

class Song (models.Model):
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
    title = models.CharField(max_length = 70)
    release_date = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.IntegerField()

    def __str__(self):
        return self.title



class Lyric (models.Model):
    song = models.ForeignKey(Song, on_delete = models.CASCADE)
    context = models.CharField(max_length = 4000)
    song_track_id = models.IntegerField()

    def __str__(self):
        return self.song_track_id

