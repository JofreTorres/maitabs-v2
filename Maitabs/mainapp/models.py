from django.db import models

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)

class Artista(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)

class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)

class Genero(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)