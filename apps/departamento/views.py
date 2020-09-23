from django.shortcuts import render
from django.views.generic import ListView
from .models import Departamento
# Create your views here.


class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name = 'departamentos'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Departamento.objects.filter(
            name__icontains=palabra_clave
        )
        return lista
