from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from paginas.models import Aluno
from django import forms
from .forms import AlunoForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import FuncionarioForm
from django.contrib.auth import logout
from django.views.generic.base import View


class IndexView(TemplateView):
    template_name = 'index.html'


def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            novo_aluno = form.save()
            # Redirecione para uma página de confirmação ou outra página relevante
            return redirect('confirmacao')
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
                return redirect('homefuncionario')
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Recupere o usuário logado (assumindo que o usuário está autenticado)
        usuario = self.request.user

        # Passe o nome do usuário no contexto
        context['nome_usuario'] = usuario.username  # Use 'username' para obter o nome do usuário

        return context


class HomefuncionarioView(TemplateView):
    template_name = 'homefuncionario.html'
# aqui sao sao os rederecionamentos


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Recupere o usuário logado (assumindo que o usuário está autenticado)
        usuario = self.request.user

        # Passe o nome do usuário no contexto
        context['nome_usuario'] = usuario.username  # Use 'username' para obter o nome do usuário

        return context

def redirecionar_login(request):
    return redirect('login_student')


def redirecionar_registro_Aluno(request):
    return redirect('cadastrar_aluno')


def redirecionar_login_funcionario(request):
    return redirect('login_funcionario')


def redirecionar_registro_Funcioario(request):
    return redirect('cadastrar_funcionario')


def redirecionar_index(request):
    return redirect('IndexView')


class CustomLogoutView(View):
    def get(self, request):
        # Adicione qualquer lógica personalizada que você deseja executar durante o logout
        # Aqui você pode, por exemplo, registrar informações sobre o usuário que está fazendo logout

        # Em seguida, realize o logout do usuário
        logout(request)

        # Redirecione para a página desejada após o logout
        return redirect('index')


def salvar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar para uma página de sucesso após o cadastro
            return redirect('pagina_sucesso')
    else:
        form = FuncionarioForm()

    return render(request, 'RegisterFuncionario.html', {'form': form})


def salvar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar para a página de confirmação
            return redirect('confirmacao')
    else:
        form = AlunoForm()

    return render(request, 'registerStudent.html', {'form': form})


def pagina_de_confirmacao(request):
    return render(request, 'pagina_de_confirmacao.html')
