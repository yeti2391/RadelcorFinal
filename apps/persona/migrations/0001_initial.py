# Generated by Django 3.1.1 on 2020-09-23 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.IntegerField(unique=True, verbose_name='Cedula')),
                ('first_name', models.CharField(max_length=60, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=60, verbose_name='apellidos')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='empleado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='correo')),
                ('numero', models.IntegerField(blank=True, null=True, verbose_name='Numero de contacto')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['last_name', 'first_name'],
                'unique_together': {('first_name', 'departamento')},
            },
        ),
    ]
