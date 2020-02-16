from django.db import models
from apps.generos.models import Genero
from apps.artistas.models import Artista
from apps.albuns.models import Album

class Musica(models.Model):
    nome = models.CharField(max_length=70)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome