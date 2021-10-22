from django.shortcuts import render, redirect
from core.models import Produto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

#def index(request):
#    return redirect('/produto/')


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuario e/ou senha inválidos')
    return redirect('/')


@login_required(login_url='/login/')
def lista_produtos(request):
    usuario = request.user
    produto = Produto.objects.filter(usuario=usuario)
    dados = {'produto': produto}
    return render(request, 'produto.html', dados)


@login_required(login_url='/login/')
def cadastro(request):
    return render(request, 'cadastro.html')


@login_required(login_url='/login/')
def submit_cadastro(request):
    if request.POST:
        nome = request.POST.get('nome')
        ncm = request.POST.get('ncm')
        valor = request.POST.get('valor')
        usuario = request.user
        Produto.objects.create(
            nome=nome,
            ncm=ncm,
            valor=valor,
            usuario=usuario
        )
        return redirect('/')
    return redirect('/')



