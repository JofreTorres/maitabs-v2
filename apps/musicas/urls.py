from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='musicas_index'),
    path('novo', views.novo, name='musicas_novo'),
    path('criar', views.criar, name='musicas_criar'),
    path('editar/<id>', views.editar, name='musicas_editar'),
    path('atualizar/<id>', views.atualizar, name='musicas_atualizar'),
    path('deletar/<id>', views.deletar, name='musicas_deletar'),
]
