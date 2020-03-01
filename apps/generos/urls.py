from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='generos_index'),
    path('novo', views.novo, name='generos_novo'),
    path('criar', views.criar, name='generos_criar'),
    path('editar/<id>', views.editar, name='generos_editar'),
    path('atualizar/<id>', views.atualizar, name='generos_atualizar'),
    path('deletar/<id>', views.deletar, name='generos_deletar'),
]
