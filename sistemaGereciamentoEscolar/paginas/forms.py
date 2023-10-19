from django import forms
from .models import Aluno,Funcionario  # Certifique-se de importar o modelo Aluno do seu aplicativo


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'  # Isso permite que o formulário inclua todos os campos do modelo Aluno
class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'  # Isso permite que o formulário inclua todos os campos do modelo Funcionario
