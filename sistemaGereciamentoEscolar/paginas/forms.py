from django import forms
# Certifique-se de importar o modelo Aluno do seu aplicativo
from .models import Aluno, Funcionario


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'  # Isso permite que o formulário inclua todos os campos do modelo Aluno


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        # Isso permite que o formulário inclua todos os campos do modelo Funcionario
        fields = '__all__'
