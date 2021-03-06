"""Maitabs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.mainapp.urls')),
    path('generos/', include('apps.generos.urls')),
    path('artistas/', include('apps.artistas.urls')),
    path('musicas/', include('apps.musicas.urls')),
    path('albuns/', include('apps.albuns.urls')),
    path('contas/', include('apps.contas.urls')),
    path('busca/', include('apps.busca.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
