from django.shortcuts import render
from rest_framework import generics
from .models import Music
from .serializers import MusicSerializer


from django.http import HttpResponse

class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
