from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('disciplina/',
         views.DisciplinaListarView.as_view(),
         name='disciplina_listar'),
    path('disciplina/criar',
         views.DisciplinaCriarView.as_view(),
         name='disciplina_criar'),
    path('disciplina/excluir/<pk>/',
         views.DisciplinaExcluirView.as_view(),
         name='disciplina_excluir'),
    path('alunopdf/', views.NotasPdfView.as_view(), name='alunopdf'),
]
