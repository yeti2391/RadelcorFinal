from django.contrib import admin
from django.urls import path

from . import views

app_name = "novedades_app"

urlpatterns = [
    path(
        'novedades-lista/',
        views.AllNovedadesListView.as_view(),
        name='novedades_list'),
    path(
        'ver-novedad/<pk>/',
        views.NovedadesViewDetail.as_view(),
        name='novedades_detail'),

]
