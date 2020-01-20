from django.db import models

class Musica(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)
    artista = models.ForeignKey('Artista', on_delete=models.CASCADE)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)

    def __str__(self):
        return "%s %s" % (self.id, self.nome)

class Artista(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)

    def __str__(self):
        return "%s %s" % (self.id, self.nome)

class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)

    def __str__(self):
        return "%s %s" % (self.id, self.nome)

class Genero(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)

    def __str__(self):
        return "%s %s" % (self.id, self.nome)

class Playlist(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)
    criador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome