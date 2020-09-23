from django.shortcuts import render
from django.views.generic import TemplateView

# Create your models here.

class InicioView(TemplateView):
    template_name= 'core/inicio.html'
