from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Tarefa
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

#pergar o usuario logado

def get_user(request):
    return request.user


#pagina incial das tarefas
class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'
   
    def get(self, request):
         context = {'usuario':get_user(request).username}
         tarefas = Tarefa.objects.filter(usuario=get_user(request).id).order_by('-id')
         context['tarefas'] = tarefas
         context['title'] = 'Home'
         return render(request, self.template_name, context)
# deixarei o cbv de lado apra usar o htmx

def htmx_criar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        concluida = True if request.POST.get('concluida') else False
        tarefa = Tarefa(usuario=get_user(request), titulo=titulo, descricao=descricao, concluida=concluida)
        tarefa.save()
        context = {'tarefas': Tarefa.objects.filter(usuario=get_user(request).id).order_by('-id')}
        return render(request,'parciais/lista_tarefas.html',context)


def htmx_listar_tarefa(request):
    tarefas = Tarefa.objects.filter(usuario=get_user().id).order_by('-id')
    context = {'tarefas':tarefas}
    return render(request, 'parciais/lista_tarefas.html',context)


def htmx_deletar_tarefa(request,tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.delete()
    tarefas = Tarefa.objects.filter(usuario=get_user(request).id).order_by('-id')
    context = {'tarefas':tarefas}
    return render(request, 'parciais/lista_tarefas.html',context)


def htmx_editar_tarefa(request,tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    if tarefa.concluida:
        checked = 'checked'
    else:
        checked = ''
    if request.method == 'POST':
        tarefa = Tarefa.objects.get(id=tarefa_id)
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        concluida = True if request.POST.get('concluida') else False
        tarefa.usuario = get_user(request)
        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.concluida = concluida
        tarefa.editada = timezone.now()
        tarefa.save()
        return redirect('home')
    
    return render(request,'atualizar_tarefa.html',{'tarefa':tarefa,'checked':checked,'title':'Editar'})


def htmx_filtrar(request):
    filtro = request.POST.get('filtro')
    try:
        tarefas = Tarefa.objects.filter(usuario=get_user(request).id, concluida=filtro).order_by('-id')
    except Exception:
        tarefas = Tarefa.objects.filter(usuario=get_user(request).id).order_by('-id')
    
    return render(request,'parciais/lista_tarefas.html',{'tarefas':tarefas})