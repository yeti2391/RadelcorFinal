from django.shortcuts import render
from django.views.generic import (ListView, DetailView)

from .models import Empleado

# Create your views here.


class ListAllEmpleado(ListView):
    """ lista empleados TOTAL """
    template_name = 'persona/list_all.html'
    context_object_name = 'empleados'
    ordering = 'last_name'
    paginate_by = 4
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            last_name__icontains=palabra_clave
        )
        return lista



class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        return context
