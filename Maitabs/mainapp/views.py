from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Musica

def home(request):
    template = loader.get_template('mainapp/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def teladelogin(request):
    template = loader.get_template('mainapp/teladelogin.html')
    context = {}
    return HttpResponse(template.render(context, request))

def listademusicas(request):
    template = loader.get_template('mainapp/listademusicas.html')
    context = {}
    return HttpResponse(template.render(context, request))
