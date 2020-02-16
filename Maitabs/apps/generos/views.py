from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import GeneroForm
from .models import Genero

def index(request):
    template = loader.get_template('generos/index.html')

    generos = Genero.objects.all()

    context = {
        'generos': generos
    }

    return HttpResponse(template.render(context, request))


def novo(request):
    template = loader.get_template('generos/novo.html')
    form = GeneroForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


def criar(request):
    form = GeneroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('generos_index')

    context = {
        'form': form
    }

    return render(request, context)


def editar(request, id):
    template = loader.get_template('generos/editar.html')

    genero = Genero.objects.get(pk=id)

    form = GeneroForm(instance=genero)

    context = {
        'form': form,
        'genero': genero
    }
    return HttpResponse(template.render(context, request))


def atualizar(request, id):
    genero = Genero.objects.get(pk=id)
    form = GeneroForm(request.POST or None, instance=genero)

    if form.is_valid():
        form.save()
        return redirect('generos_index')

    context = {
        'form': form
    }

    return render(request, context)


def deletar(request, id):
    genero = Genero.objects.get(pk=id)
    genero.delete()
    return redirect('generos_index')
