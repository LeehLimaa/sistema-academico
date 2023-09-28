from django.db import models

class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome_cidade}, {self.uf}"

class Ocupacao(models.Model):
    nome_ocupacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_ocupacao

class Pessoas(models.Model):
    nome_pessoa = models.CharField(max_length=100)
    nome_pai = models.CharField(max_length=100)
    nome_mae = models.CharField(max_length=100)
    cpf_pessoa = models.CharField(max_length=11, unique=True)
    data_nasc_pessoa = models.DateField()
    email_pessoa =  models.CharField(max_length=100)
    cidade_pessoa = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ocupacao_pessoa = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_pessoa

class Instituicoes(models.Model):
    nome_instituicao = models.CharField(max_length=100)
    site_instituicao = models.CharField(max_length=100)
    telefone_instituicao = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.nome_instituicao

class Areas(models.Model):
    nome_area = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_area
   
class Cursos(models.Model):
    nome_curso = models.CharField(max_length=100)
    carga_horaria_total_curso = models.CharField(max_length=10)
    duracao_meses_curso = models.IntegerField()
    area_curso = models.ForeignKey(Areas, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicoes, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_curso

class Semestres(models.Model):
    quantidade_periodo = models.CharField(max_length=2)

    def __str__(self):
        return self.quantidade_periodo
    
class Disciplinas(models.Model):
    nome_disciplina = models.CharField(max_length=100)
    area_disciplina = models.ForeignKey(Areas, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_disciplina

class Matriculas(models.Model):
    instituicao_matricula = models.ForeignKey(Instituicoes, on_delete=models.CASCADE)
    curso_matricula = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    pessoa_matricula = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    data_inicio_matricula = models.DateField()
    data_previsao_termino_matricula = models.DateField()

    def __str__(self):
        return f"{self.instituicao_matricula}, {self.curso_matricula}, {self.pessoa_matricula}"

class Tipo_avaliacao(models.Model):
    tipo_avaliacao = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_avaliacao

class Avaliacoes(models.Model):
    descricao_avaliacao = models.TextField()
    curso_avaliacao = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    pessoa_avaliacao = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    tipo_avaliacao = models.ForeignKey(Tipo_avaliacao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descricao_avaliacao}, {self.curso_avaliacao}, {self.pessoa_avaliacao}"

class Frequencias(models.Model):
    curso_frequencia = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina_frequencia = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField()

    def __str__(self):
        return f"{self.curso_frequencia}, {self.disciplina_frequencia}, {self.numero_faltas}"

class Turnos(models.Model):
    nome_turno = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_turno

class Turmas(models.Model):
    nome_turma = models.CharField(max_length=100)
    periodo_semestre_turma = models.IntegerField()
    turno_turma = models.ForeignKey(Turnos, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_turma
    
class Ocorrencias(models.Model):
    descricao_ocorrencia = models.TextField()
    data_ocorrencia = models.DateField()
    curso_ocorrencia = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina_ocorrencia = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    pessoa_ocorrencia = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.descricao_ocorrencia}, {self.data_ocorrencia}, {self.pessoa_ocorrencia}"
    
class Disciplinas_cursos(models.Model):
    nome_disciplina_curso = models.CharField(max_length=100)
    carga_horaria_disciplina_curso = models.CharField(max_length=10)
    curso_disciplina_curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    semestres_disciplina_curso = models.CharField(max_length=2)
    
    def __str__(self):
        return self.nome_disciplina_curso
