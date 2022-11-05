from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Artist, Song, Lyric
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ArtistSerializer, SongSerializer, LyricSerializer
from urllib import response
from django.shortcuts import render



#Create your views here.

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]




  

class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]


class LyricViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer
    permission_classes = [permissions.IsAuthenticated]