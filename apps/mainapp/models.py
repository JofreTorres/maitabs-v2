from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=70)

    def __str__(self):
        return "%s" % (self.nome)

class Playlist(models.Model):
    nome = models.CharField(max_length=70)
    criador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
