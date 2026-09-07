from django.db import models

# Create your models here.
class Music(models.Model):
    class Meta:
        db_table = 'music'

    title = models.CharField(max_length=100)
    seconds = models.IntegerField()


    def __str__(self):
        return self.title

class Musician(models.Model):
    class Meta:
        db_table = 'musician'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Instrument(models.Model):
    class Meta:
        db_table = 'instrument'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Band(models.Model):
    class Meta:
        db_table = 'band'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    typeofmusic = models.CharField(max_length=100)
    numberofmembers = models.IntegerField()

class Teste(models.Model):
    class Meta:
        db_table = 'teste'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)