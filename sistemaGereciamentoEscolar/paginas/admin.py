from django.contrib import admin
from .models import Aluno, Usuario, Funcionario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['user', 'cpf', 'endereco',
                    'telefone', 'data_nascimento', 'genero']


class AlunoAdmin(admin.ModelAdmin):
    list_display = ['user', 'cpf', 'endereco', 'telefone',
                    'data_nascimento', 'genero', 'matricula']


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['user', 'cpf', 'endereco', 'telefone',
                    'data_nascimento', 'genero', 'cargo', 'salario']


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
