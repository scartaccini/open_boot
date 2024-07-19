from django.contrib import admin
from django.urls import path, include
from .views import index, crea_grafiti, edita_grafiti, elimina_grafiti, busca_grafiti

urlpatterns = [    
    path('', index, name='index'),
    path('crear/', crea_grafiti, name='crea_grafiti'),
    path('editar/<int:id_grafiti>/', edita_grafiti, name='edita_grafiti'),
    path('eliminar/<int:id_grafiti>/', elimina_grafiti, name='elimina_grafiti'),
    path('buscar/', busca_grafiti, name='busca_grafiti'),
    
]
