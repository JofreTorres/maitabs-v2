from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=70)

    def __str__(self):
        return "%s" % (self.nome)
