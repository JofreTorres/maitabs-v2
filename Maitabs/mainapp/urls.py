from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teladelogin', views.teladelogin, name='teladelogin'),
    path('listademusicas', views.listademusicas, name='listademusicas')
]
