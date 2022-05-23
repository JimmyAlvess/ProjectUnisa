from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Medico

# Create your views here.


def home(request):
    medicos = Medico.objects.filter(
        publicado=True
    ).order_by('-id')

    return render(request, 'consulta/pages/home.html', context={
        'medicos': medicos
    })


def especialidade(request, especialidade_id):
    medicos = get_list_or_404(Medico, publicado=True,
                              especialidade__id=especialidade_id)

    return render(request, 'consulta/pages/especialidade.html', context={
        'medicos': medicos
    })


def search(request):
    search_term = request.GET.get('search', '').strip()
    if not search_term:
        raise Http404()
    medicos = Medico.objects.filter(
        Q(
            Q(nome_completo__icontains=search_term) |
            Q(crm__icontains=search_term),
        ),
        publicado=True
    ).order_by('-id')

    return render(request, 'consulta/pages/search.html', context={
        'search_term': search_term,
        'medicos': medicos
    })


def medico(request, id):
    medico = get_object_or_404(Medico, publicado=True, pk=id)

    return render(request, 'consulta/pages/medico.html', context={
        'medico': medico
    })
