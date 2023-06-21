from django.shortcuts import render, redirect
from .models import Tarefa

def home(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'home.html', {'tarefas': tarefas})

def salvar(request):
    nova_tarefa = Tarefa()
    nova_tarefa.tarefa =  request.POST.get('tarefa')

    prazo = request.POST.get('prazo')
    if prazo:
        nova_tarefa.prazo =  prazo

    nova_tarefa.save()

    tarefas = Tarefa.objects.all()
    return render(request, 'home.html', {'tarefas': tarefas})

def editar(request, id):
    tarefa = Tarefa.objects.get(id=id)
    return render(request, 'update.html',{'tarefa': tarefa})

def update(request, id):
    tarefa =  request.POST.get('tarefa')

    prazo = request.POST.get('prazo')
    if prazo:
        prazo =  prazo

    nova_tarefa = Tarefa.objects.get(id=id)
    nova_tarefa.tarefa = tarefa
    nova_tarefa.prazo = prazo
    nova_tarefa.save()

    return redirect(home)

def excluir(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect(home)

def meusdados(request):
    return render(request, 'meusdados.html')