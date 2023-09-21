"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('cidade/', cidade, name='cidades'),
    path('pessoa/', pessoa, name='pessoa'),
    path('ocupacao/', ocupacao, name='ocupacao'),
    path('instituicao/', instituicao, name='instituicao'),
    path('area/', area, name='area'),
    #path('cursos/', curso, name='cursos'),
    #path('semestres/', semestre, name='semestres'),
    #path('disciplinas/', disciplina, name='disciplinas'),
    #path('matriculas/', matricula, name='matriculas'),
    #path('tipos_avaliacoes/', tipo_avaliacao, name='tipos_avaliacoes'),
    #path('avaliacoes/', avaliacao, name='avaliacoes'),
    #path('frequencia/', frequencia, name='frequencia'),
    #path('turmas/', turma, name='turmas'),
    #path('ocorrencias/', ocorrencia, name='ocorrencias'),
    #path('disciplinas_cursos/', disciplina_curso, name='disciplinas_cursos'),
]
