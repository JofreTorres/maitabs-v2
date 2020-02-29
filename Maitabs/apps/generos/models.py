from django.db import models
from django.utils.text import slugify

class Genero(models.Model):
    nome = models.CharField(max_length=70)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Genero, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % (self.nome)
