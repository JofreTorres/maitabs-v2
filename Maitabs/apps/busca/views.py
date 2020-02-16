from django.template import loader
from django.http import HttpResponse
from apps.musicas.models import Musica

def index(request):
    template = loader.get_template('busca/index.html')

    musicas = Musica.objects.all()
    
    context = {
        'musicas': musicas
    }

    return HttpResponse(template.render(context, request))
