from django.db import models

class Musica(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)
    artista = models.ForeignKey('Artista', on_delete=models.CASCADE)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    def __str__(self):
        return self.Musica

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)

    def __str__(self):
        return "%s %s" % (self.id, self.name)

class Artista(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)

    def __str__(self):
        return "%s %s" (self.id, self.name)

class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)

    def __str__(self):
        return "%s %s" (self.id, self.name)

class Genero(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)

    def __str__(self):
        return "%s %s" (self.id, self.name)

class Playlist(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)
    criador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.Playlist
