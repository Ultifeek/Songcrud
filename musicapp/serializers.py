from rest_framework import serializers
from .models import Artist, Song, Lyric
\

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['first_name', 'last_name', 'age']


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['artist', 'title', 'release_date', 'likes', 'artiste_id']


class LyricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lyric
        fields = ['song','context', 'song_track_id']