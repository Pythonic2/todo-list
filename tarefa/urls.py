from django.urls import path
from .views import HomeView,htmx_criar_tarefa,htmx_listar_tarefa,htmx_deletar_tarefa,htmx_editar_tarefa,htmx_filtrar

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('criar-tarefas/',htmx_criar_tarefa,name='criar'),
    path('lista-tarefas/',htmx_listar_tarefa,name='listar'),
    path('deletar-tarefas/<int:tarefa_id>',htmx_deletar_tarefa,name='deletar'),
    path('editar-tarefas/<int:tarefa_id>',htmx_editar_tarefa,name='editar'),
    path('filtrar/',htmx_filtrar,name='filtrar'),
]
