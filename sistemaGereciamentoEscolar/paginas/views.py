from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from paginas.models import Aluno
from django import forms
from .forms import AlunoForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import FuncionarioForm


class IndexView(TemplateView):
    template_name = 'index.html'


def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            novo_aluno = form.save()
            # Redirecione para uma página de confirmação ou outra página relevante
            return redirect('pagina_de_confirmacao')
    else:
        form = AlunoForm()

    return render(request, 'registerStudent.html', {'form': form})


def login_student(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirecione para a página após o login bem-sucedido
                return redirect('home')
            else:
                messages.error(
                    request, 'Credenciais inválidas. Tente novamente.')
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
    else:
        form = AuthenticationForm()

    return render(request, 'loginStudent.html', {'form': form})


def cadastrar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            novo_funcionario = form.save()
            # Redirecione para uma página de confirmação ou outra página relevante
            return redirect('pagina_de_confirmacao')
    else:
        form = FuncionarioForm()

    return render(request, 'RegisterFuncionario.html', {'form': form})
    
def login_funcionario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirecione para a página após o login bem-sucedido
                return redirect('pagina_apos_login')
            else:
                messages.error(
                    request, 'Credenciais inválidas. Tente novamente.')
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
    else:
        form = AuthenticationForm()

    return render(request, 'loginfuncionario.html', {'form': form})

class HomeView(TemplateView):
    template_name = 'home.html'


# aqui sao sao os rederecionamentos
def redirecionar_login(request):
    return redirect('login_student')


def redirecionar_registro_Aluno(request):
    return redirect('cadastrar_aluno')
