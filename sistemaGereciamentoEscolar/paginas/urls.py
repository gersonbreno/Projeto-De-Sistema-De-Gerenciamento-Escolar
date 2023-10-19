from django.urls import path

from .views import IndexView, HomeView, cadastrar_aluno
from . import views


urlpatterns = [
    path('', IndexView.as_view(), ),  # Use as_view() method here
    path('home/', HomeView.as_view(), name='home'),
    path('cadastrar_aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('cadastrar_funcionario/', views.cadastrar_funcionario,
         name='cadastrar_funcionario'),
    path('login_funcionario/', views.login_funcionario, name='login_funcionario'),
    path('login_Student/', views.login_student, name='login_student'),
    path('redirecionar-login/', views.redirecionar_login,
         name='redirecionar_login'),
    path('redirecionar_registro_Aluno/', views.redirecionar_registro_Aluno,
         name='redirecionar_registro_Aluno'),
]
