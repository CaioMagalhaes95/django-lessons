from rest_framework import serializers
from .models import Band, Instrument, Music, Musician, Teste

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'

class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teste
        fields = '__all__'