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
    path('curso/', curso, name='curso'),
    path('semestre/', semestre, name='semestre'),
    path('disciplina/', disciplina, name='disciplina'),
    path('matricula/', matricula, name='matricula'),
    path('tipo_avaliacao/', tipo_avaliacao, name='tipo_avaliacao'),
    path('avaliacao/', avaliacao, name='avaliacao'),
    path('frequencia/', frequencia, name='frequencia'),
    path('turma/', turma, name='turma'),
    path('ocorrencia/', ocorrencia, name='ocorrencia'),
    path('disciplina_curso/', disciplina_curso, name='disciplina_curso'),
]
