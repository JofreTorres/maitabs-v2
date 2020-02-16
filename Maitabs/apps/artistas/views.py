from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import ArtistaForm
from .models import Artista

def index(request):
    template = loader.get_template('artistas/index.html')

    artistas = Artista.objects.all()

    context = {
        'artistas': artistas
    }

    return HttpResponse(template.render(context, request))


def novo(request):
    template = loader.get_template('artistas/novo.html')
    form = ArtistaForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


def criar(request):
    form = ArtistaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form
    }

    return render(request, context)


def editar(request, id):
    template = loader.get_template('artistas/editar.html')

    artista = Artista.objects.get(pk=id)

    form = ArtistaForm(instance=artista)

    context = {
        'form': form,
        'artista': artista
    }
    return HttpResponse(template.render(context, request))


def atualizar(request, id):
    artista = Artista.objects.get(pk=id)
    form = ArtistaForm(request.POST or None, instance=artista)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form
    }

    return render(request, context)


def deletar(request, id):
    artista = Artista.objects.get(pk=id)
    artista.delete()
    return redirect('index')
