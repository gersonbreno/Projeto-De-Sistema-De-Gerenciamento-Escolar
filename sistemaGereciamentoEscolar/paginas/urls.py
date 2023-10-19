from django.urls import path

from .views import IndexView, HomeView, cadastrar_aluno,  HomefuncionarioView, CustomLogoutView
from . import views


urlpatterns = [
    path('', IndexView.as_view(),  name='index'),  # Use as_view() method here
    path('home/', HomeView.as_view(), name='home'),
    path('homefuncionario/', HomefuncionarioView.as_view(), name='homefuncionario'),
    path('cadastrar_aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastrar_funcionario/', views.cadastrar_funcionario,
         name='cadastrar_funcionario'),
    path('login_funcionario/', views.login_funcionario, name='login_funcionario'),
    path('login_Student/', views.login_student, name='login_student'),

    # redireconamento
    path('redirecionar-login/', views.redirecionar_login,
         name='redirecionar_login'),
    path('redirecionar_registro_Aluno/', views.redirecionar_registro_Aluno,
         name='redirecionar_registro_Aluno'),
    # funcionario

    path('redirecionar_registro_Funcioario/', views.redirecionar_registro_Funcioario,
         name='redirecionar_registro_Funcioario'),

    path('redirecionar_login_funcionario/', views.redirecionar_login_funcionario,
         name='redirecionar_login_funcionario'),
    path('redirecionar_index/', views.redirecionar_index,
         name='redirecionar_index'),
    path('custom_logout/', CustomLogoutView.as_view(), name='custom_logout'),
    path('salvar_funcionario/', views.salvar_funcionario,
         name='salvar_funcionario'),
          path('salvar_aluno/', views.salvar_aluno, name='salvar_aluno'),


]
