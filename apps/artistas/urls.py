from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='artistas_index'),
    path('novo', views.novo, name='artistas_novo'),
    path('criar', views.criar, name='artistas_criar'),
    path('editar/<id>', views.editar, name='artistas_editar'),
    path('atualizar/<id>', views.atualizar, name='artistas_atualizar'),
    path('deletar/<id>', views.deletar, name='artistas_deletar'),
]
