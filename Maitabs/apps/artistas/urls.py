from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novo', views.novo, name='novo'),
    path('criar', views.criar, name='criar'),
    path('editar/<id>', views.editar, name='editar'),
    path('atualizar/<id>', views.atualizar, name='atualizar'),
    path('deletar/<id>', views.deletar, name='deletar'),
]