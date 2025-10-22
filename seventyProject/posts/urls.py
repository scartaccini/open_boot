from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.autores, name="autores"),
    path('autores_limite/', views.autores_limite, name="autores_limite"),
    path('autor/', views.autor, name="autor"),
    path('autor_id/', views.autor_id, name="autor_id"),
    path('actualizacion/', views.actualizacion, name="actualizacion"),
    path('actualizacionEntry/', views.actualizacion_entry, name="actualizacion_entry"),
    path('eliminarAutor/', views.eliminar_autor, name="elimina_autor"),
    path('mostrarEntradas/', views.mostrar_entradas, name="listar_entradas"),
    path('crearEntrada/', views.crear_entrada, name="crear_entrada"),
    path('eliminarEntrada/', views.eliminarEntrada, name="eliminarEntrada"),
]