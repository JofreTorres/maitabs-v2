from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='contas_index'),
    path('nova', views.nova, name='contas_nova'),
    path('mudar_senha', views.mudar_senha, name='contas_mudar_senha'),
    path('login', views.login, name='contas_login'),
    path('logout', views.logout, name='contas_logout'),
]
