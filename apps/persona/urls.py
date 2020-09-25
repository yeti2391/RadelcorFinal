from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"


urlpatterns = [
    path(
        'ver-empleado/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
    ),
    path(
        'list-all/',
        views.ListAllEmpleado.as_view(),
        name='empleados_total'
    ),
    #SE AGREGA EL SIGUIENTE PATH PARA EL FILTRO POR AREA
    path(
        'list_by_area/<shorname>/',
        views.ListByAreaEmpleado.as_view(),
        name = 'empleados_area'
    ),

]
