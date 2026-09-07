from symtable import Class

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Band, Instrument, Music, Musician, Teste
from .serializers import BandSerializer, MusicSerializer, MusicianSerializer, InstrumentSerializer, TestSerializer
from django.http import HttpResponse, request

class TesteAPIView(APIView):
    queryset = Teste.objects.all()

    def get(self, request):
        teste = Teste.objects.all()
        serializer = TestSerializer(teste, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
class TesteDetailAPIView(APIView):
    queryset = Teste.objects.all()

    def get(self, request, pk):
        teste = Teste.objects.get(pk=pk)
        serializer = TestSerializer(teste)
        return Response(serializer.data)

    def put(self, request, pk):
        teste = Teste.objects.get(pk=pk)
        serializer = TestSerializer(teste, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        teste = Teste.objects.get(pk=pk)
        teste.delete()
        return Response(status=204)

class TesteList(generics.ListCreateAPIView):
    queryset = Teste.objects.all()
    serializer_class = TestSerializer

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

class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

