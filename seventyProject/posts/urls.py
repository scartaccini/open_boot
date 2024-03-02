from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.autores, name="autores"),
    path('autores_limite/', views.autores_limite, name="autores_limite"),
    path('autor/', views.autor, name="autor"),
    path('autor_id/', views.autor_id, name="autor_id"),
    path('actualizacion/', views.actualizacion, name="actualizacion"),
    
]