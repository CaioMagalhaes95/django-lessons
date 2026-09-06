from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Instrument, Music, Musician
from .serializers import MusicSerializer, MusicianSerializer, InstrumentSerializer


from django.http import HttpResponse, request

class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MusicianList(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

class MusicianDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

class InstrumentList(generics.ListCreateAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer

class InstrumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer

# @api_view(['PUT', 'DELETE'])
# def musician_detail(request, pk):
#     try:
#         musician = Musician.objects.get(pk=pk)
#     except Musician.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'PUT':
#         serializer = MusicianSerializer(musician, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         musician.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    
