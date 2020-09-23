from django.shortcuts import render
from .models import Novedades
from django.views.generic import(ListView, DetailView)



# Create your views here.
class AllNovedadesListView(ListView):
    template_name = "novedades/novedades.html"
    model = Novedades
    orderin = 'id'
    context_object_name = 'novedades'

    def get_queryset(self):
        # el codigo que yo queira
        palabra_clave = self.request.GET.get("kword", '')
        lista = Novedades.objects.filter(titulo__icontains=palabra_clave)

        return lista



class NovedadesViewDetail(DetailView):
    model = Novedades
    template_name = "novedades/detail_novedades.html"

    def get_context_data(self, **kwargs):
        context = super(NovedadesViewDetail, self).get_context_data(**kwargs)
        #toot un proceso
        context['titulo'] = 'Novedad de importancia'
        return context
