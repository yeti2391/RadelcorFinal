from django.db import models
from django.utils.timezone import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from apps.persona.models import Empleado

class Novedades(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length= 90, null=False, blank=False)
    contenido = RichTextUploadingField()
    autor = models.ForeignKey(Empleado, on_delete = models.CASCADE)
    fecha_creacion = models.DateTimeField(verbose_name='Fecha', auto_now_add=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='fecha de edicion')

    class Meta:
        verbose_name='Novedad'
        verbose_name_plural= 'Novedades'
        ordering = ['fecha_creacion']

    def __str__(self):
        return "%s %s %s %s" % (self.id, self.titulo, self.autor.first_name, self.fecha_creacion)
        """ otra forma de escribir misma linea:"""
        #return str(self.id) + '-' + self.titulo + '-' + self.autor.first_name + '-' + self.fecha_creacion
