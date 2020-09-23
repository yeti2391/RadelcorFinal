from django.shortcuts import render
from django.views.generic import (ListView, DetailView)

from .models import Empleado

# Create your views here.


class ListByAreaEmpleado(ListView):
    """ lista empleados TOTAL """
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    ordering = 'last_name'
    paginate_by = 4
    def get_queryset(self):
        # el codigo que yo queira
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
        #toot un proceso
        context['titulo'] = 'Empleado del mes'
        return context
