from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='albuns_index'),
    path('novo', views.novo, name='albuns_novo'),
    path('criar', views.criar, name='albuns_criar'),
    path('editar/<id>', views.editar, name='albuns_editar'),
    path('atualizar/<id>', views.atualizar, name='albuns_atualizar'),
    path('deletar/<id>', views.deletar, name='albuns_deletar'),
]
