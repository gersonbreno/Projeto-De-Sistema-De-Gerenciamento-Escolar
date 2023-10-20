from django.contrib import admin
from .models import Aluno, Usuario, Funcionario, Mensalidade, Alimentacao


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'user', 'cpf', 'endereco',
                    'telefone', 'data_nascimento', 'genero']


class AlunoAdmin(admin.ModelAdmin):
    list_display = ['user', 'cpf', 'endereco', 'telefone',
                    'data_nascimento', 'genero', 'matricula']


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['user', 'cpf', 'endereco', 'telefone',
                    'data_nascimento', 'genero', 'cargo', 'salario']


class MensalidadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'valor', 'aluno']

    def aluno_nome(self, obj):
        return obj.aluno.nome


class AlimentacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cardapio', 'fornecedor', 'estoque']


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Alimentacao, AlimentacaoAdmin)

admin.site.register(Mensalidade, MensalidadeAdmin)
