from django.db import models

# Create your models here.
class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=
    nome = models.CharField(max_length

    nome =
100)
    cpf = models.CharField(max_length=
    cpf = models.CharField
14)
    endereco = models.TextField()
    telefone = models.CharField(max_length=
    endereco = models.TextField()
    telefone = models.CharField(
    endereco = models.TextField()
    telefone = models.CharField

    endereco = models.TextField()
    telefone = models

    endereco = models.TextField()
    telefone =

    endereco = models.TextField()
    telefone

    endereco = models.TextField()

    endereco = models.TextField

    endereco
15)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    matricula = models.CharField(max_length=
    matricula = models.CharField(max_length=

    matricula = models.CharField(max_length

    matricula = models.CharField(
    matricula = models.CharField

    matricula = models

    matricula

    mat

   
10)
    mensalidade = models.DecimalField(max_digits=
    mensalidade = models.DecimalField(max_digits

    mensal
6, decimal_places=2)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

    
    pessoa = models.OneToOneField(Pessoa,

    pessoa = models.OneToOneField(Pessoa

    pessoa = models.OneToOneField(P

    pessoa = models.OneToOneField

    pessoa =
def calcular_media(self):
        # Implemente a lógica para calcular a média do aluno aqui
        pass

    def criar_conta(self):
        # Implemente a lógica para criar uma conta do aluno aqui
        pass

    def realizar_login(self):
        # Implemente a lógica para realizar o login do aluno aqui
        pass

    def __str__(self):
        return f"Aluno: {self.pessoa.nome}, Matrícula: {self.matricula}"