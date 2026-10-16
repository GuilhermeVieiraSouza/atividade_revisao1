from django.shortcuts import render, get_object_or_404

from .models import Evento, Local, Relatorio

# Create your views here.

def index(request):
    eventos = Evento.objects.all()
    context = {
        'eventos': eventos
    }
    return render(request, 'eventos/index.html', context)

def detalhe(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    atividades = evento.atividades.all()
    relatorio = Relatorio.objects.filter(evento=evento).first()
    
    context = {
        'evento': evento,
        'atividades': atividades,
        'relatorio': relatorio
    }
    
    return render(request, 'eventos/detalhe.html', context)

def local(request, local_id):
    local = get_object_or_404(Local, pk=local_id)
    eventos = local.eventos.all()
    
    context = {
        'local': local,
        'eventos': eventos
    }
    
    return render(request, 'eventos/local.html', context)   