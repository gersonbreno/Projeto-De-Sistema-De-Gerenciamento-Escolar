from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.TextField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField(default='2000-01-01')
    genero_choices = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    # Exemplo de valor padrão
    genero = models.CharField(
        max_length=1, choices=genero_choices, default='M')
# cadastro de alunos


class Aluno(Usuario):
    matricula = models.CharField(max_length=20)

# classe de funcionarios


class Funcionario(Usuario):
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
