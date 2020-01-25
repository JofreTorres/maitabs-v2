from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import GeneroForm

def index(request):
    template = loader.get_template('generos/index.html')
    context = {}
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
        return redirect('index')

    context = {
        'form': form
    }

    return render(request, context)
