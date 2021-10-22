from django.shortcuts import render, redirect
from core.models import Produto
# Create your views here.

#def index(request):
#    return redirect('/produto/')

def lista_produtos(request):
    #usuario = request.user
    produto = Produto.objects.all()
    dados = {'produto': produto}
    return render(request, 'produto.html', dados)



