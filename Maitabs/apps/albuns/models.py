from django.db import models
from django.utils.text import slugify

class Album(models.Model):
    nome = models.CharField(max_length=70)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        musica_slug = self.artista.nome + "-" + self.nome
        self.slug = slugify(musica_slug)
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % (self.nome)
