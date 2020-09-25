from django.shortcuts import render
from django.urls import reverse, reverse_lazy
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



class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista
