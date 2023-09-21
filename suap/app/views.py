from django.shortcuts import render
from . models import *

def cidade(request):
    cidades = {
         'cidades':Cidade.objects.all()
        }

    return render(request,'cidade/cidade.html',cidades)

def pessoa(request):
    pessoas = {
         'pessoas':Pessoas.objects.all()
        }

    return render(request,'pessoa/pessoa.html', pessoas)

def ocupacao(request):
    ocupacaos = {
         'ocupacaos':Ocupacao.objects.all()
        }

    return render(request,'ocupacao/ocupacao.html', ocupacaos)

def instituicao(request):
    instituicoes = {
         'instituicoes':Instituicoes.objects.all()
        }

    return render(request,'instituicao/instituicao.html', instituicoes)

def area(request):
    areas = {
         'areas':Areas.objects.all()
        }

    return render(request,'area/area.html', areas)
