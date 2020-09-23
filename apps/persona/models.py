from django.db import models

# Create your models here.
from apps.departamento.models import Departamento



# Create your models here.
class Empleado(models.Model):
    """ Modelo para tabla empleado """
    id = models.AutoField(primary_key = True)
    cedula = models.IntegerField('Cedula', blank=False, null=False, unique=True)
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('apellidos', max_length=60)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    email = models.EmailField(blank = True, verbose_name='correo', null=True)
    numero = models.IntegerField('Numero de contacto', blank=True, null=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['last_name', 'first_name']
        unique_together = ('first_name', 'departamento')


    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
