from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import MusicaForm
from .models import Musica

def index(request):
    template = loader.get_template('musicas/index.html')

    musicas = Musica.objects.all()

    context = {
        'musicas': musicas
    }

    return HttpResponse(template.render(context, request))


def novo(request):
    template = loader.get_template('musicas/novo.html')
    form = MusicaForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


def criar(request):
    form = MusicaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('musicas_index')
    else:
        template = loader.get_template('musicas/novo.html')

        context = {
            'form': form
        }

        return HttpResponse(template.render(context, request))


def editar(request, id):
    template = loader.get_template('musicas/editar.html')

    musica = Musica.objects.get(pk=id)

    form = MusicaForm(instance=musica)

    context = {
        'form': form,
        'musica': musica
    }
    return HttpResponse(template.render(context, request))


def atualizar(request, id):
    musica = Musica.objects.get(pk=id)
    form = MusicaForm(request.POST or None, instance=musica)

    if form.is_valid():
        form.save()
        return redirect('musicas_index')

    context = {
        'form': form
    }

    return render(request, context)


def deletar(request, id):
    musica = Musica.objects.get(pk=id)
    musica.delete()
    return redirect('musicas_index')




# Create your views here.
