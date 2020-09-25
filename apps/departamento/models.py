from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50,)
    #PARA FUNCION DE FILTRADO POR AREA:
    shor_name = models.CharField('Nombre Corto', max_length=4, unique=True)

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name
