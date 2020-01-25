from django.contrib import admin
from .models import Musica
from .models import Album
from .models import Genero
from .models import Artista
from .models import Playlist
from .models import Usuario

admin.site.register(Musica)
admin.site.register(Album)
admin.site.register(Genero)
admin.site.register(Artista)
admin.site.register(Playlist)
admin.site.register(Usuario)