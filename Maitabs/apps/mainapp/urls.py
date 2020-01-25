from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teladelogin', views.teladelogin, name='teladelogin'),
    path('listademusicas', views.listademusicas, name='listademusicas'),
    path('profile', views.profile, name='profile'),
    path('visualizacao', views.visualizacao, name='visualizacao'),
    path('listapop', views.listapop, name='listapop'),
    path('listarock', views.listarock, name='listarock'),
    path('listaeletronica', views.listaeletronica, name='listaeletronica'),
    path('listareggae', views.listareggae, name='listareggae'),
    path('listahhrap', views.listahhrap, name='listahhrap'),
    path('listasoundtrack', views.listasoundtrack, name='listasoundtrack')
]
