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

def curso(request):
    cursos = {
         'cursos':Cursos.objects.all()
        }

    return render(request,'curso/curso.html', cursos)

def semestre(request):
    semestres = {
         'semestres':Semestres.objects.all()
        }

    return render(request,'semestre/semestre.html', semestres)

def disciplina(request):
    disciplinas = {
         'disciplinas':Disciplinas.objects.all()
        }

    return render(request,'disciplina/disciplina.html', disciplinas)

def matricula(request):
    matriculas = {
         'matriculas':Matriculas.objects.all()
        }

    return render(request,'matricula/matricula.html', matriculas)

def tipo_avaliacao(request):
    tipo_avaliacoes = {
         'tipo_avaliacoes':Tipo_avaliacao.objects.all()
        }

    return render(request,'tipo_avaliacao/tipo_avaliacao.html', tipo_avaliacoes)

def avaliacao(request):
    avaliacoes = {
         'avaliacoes':Avaliacoes.objects.all()
        }

    return render(request,'avaliacao/avaliacao.html', avaliacoes)

def frequencia(request):
    frequencias = {
         'frequencias':Frequencias.objects.all()
        }

    return render(request,'frequencia/frequencia.html', frequencias)

def turma(request):
    turmas = {
         'turmas':Turmas.objects.all()
        }

    return render(request,'turma/turma.html', turmas)

def ocorrencia(request):
    ocorrencias = {
         'ocorrencias':Ocorrencias.objects.all()
        }

    return render(request,'ocorrencia/ocorrencia.html', ocorrencias)

def disciplina_curso(request):
    disciplinas_cursos = {
         'disciplinas_cursos':Disciplinas_cursos.objects.all()
        }

    return render(request,'disciplina_curso/disciplina_curso.html', disciplinas_cursos)
