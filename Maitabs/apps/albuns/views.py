from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import AlbumForm
from .models import Album

def index(request):
    template = loader.get_template('albuns/index.html')

    albuns = Album.objects.all()

    context = {
        'albuns': albuns
    }

    return HttpResponse(template.render(context, request))


def novo(request):
    template = loader.get_template('albuns/novo.html')
    form = AlbumForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


def criar(request):
    form = AlbumForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form
    }

    return render(request, context)


def editar(request, id):
    template = loader.get_template('albuns/editar.html')

    album = Album.objects.get(pk=id)

    form = AlbumForm(instance=album)

    context = {
        'form': form,
        'album': album
    }
    return HttpResponse(template.render(context, request))


def atualizar(request, id):
    album = Album.objects.get(pk=id)
    form = AlbumForm(request.POST or None, instance=album)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form
    }

    return render(request, context)


def deletar(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('index')



