# Generated by Django 3.1.1 on 2020-09-23 23:47

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Novedades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=90, verbose_name='Titulo')),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='fecha de edicion')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.empleado')),
            ],
            options={
                'verbose_name': 'Novedad',
                'verbose_name_plural': 'Novedades',
                'ordering': ['fecha_creacion'],
            },
        ),
    ]
