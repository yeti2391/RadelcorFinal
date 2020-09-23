from django.contrib import admin
from django.urls import path
from .views import InicioView

app_name='core_app'

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
]
