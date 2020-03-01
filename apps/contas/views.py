from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def index(request):
    if request.user.is_authenticated:
        template = loader.get_template('contas/index.html')
        return HttpResponse(template.render({}, request))
    else:
        return redirect('contas_login')


def nova(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', None)
        user_email = request.POST.get('user_email', None)
        user_password = request.POST.get('user_password', None)

        user = User.objects.create_user(user_name, user_email, user_password)

        return redirect('contas_index')
    else:
        template = loader.get_template('contas/nova.html')
        return HttpResponse(template.render({}, request))


def mudar_senha(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', None)
        nova_senha = request.POST.get('user_password', None)

        user = User.objects.get(username=user_name)
        if user:
            user.set_password(nova_senha)
            user.save()

            print('mudar senha!')
            print(user.username)

        return redirect('contas_index')
    else:
        template = loader.get_template('contas/mudar_senha.html')
        return HttpResponse(template.render({}, request))

def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', None)
        nova_senha = request.POST.get('user_password', None)

        user = authenticate(username=user_name, password=nova_senha)

        if user:
            print('USER AUTENTICADO!')
            auth_login(request, user)
            return redirect('contas_index')
        else:
            print('USER INVALIDO')
            template = loader.get_template('contas/login.html')
            return HttpResponse(template.render({}, request))


    else:
        template = loader.get_template('contas/login.html')
        return HttpResponse(template.render({}, request))


def logout(request):
    auth_logout(request)
    return redirect('home')
