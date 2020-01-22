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

def profile(request):
    template = loader.get_template('mainapp/profile.html')
    context = {}
    return HttpResponse(template.render(context, request))

def visualizacao(request):
    template = loader.get_template('mainapp/visualizacao.html')
    context = {}
    return HttpResponse(template.render(context, request))

def listapop(request):
    template = loader.get_template('mainapp/listapop.html')
    context = {}
    return HttpResponse(template.render(context, request))

def listarock(request):
    template = loader.get_template('mainapp/listarock.html')
    context = {}
    return HttpResponse(template.render(context, request))

def listaeletronica(request):
    template = loader.get_template('mainapp/listaeletronica.html')
    context = {}
    return HttpResponse(template.render(context, request))

def listareggae(request):
    template = loader.get_template('mainapp/listareggae.html')
    context = {}
    return HttpResponse(template.render(context, request))

def listasoundtrack(request):
    template = loader.get_template('mainapp/listasoundtrack.html')
    context = {}
    return HttpResponse(template.render(context, request))

def listahhrap(request):
    template = loader.get_template('mainapp/listahhrap.html')
    context = {}
    return HttpResponse(template.render(context, request))
