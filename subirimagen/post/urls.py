from django.urls import path
from . import views

urlpatterns = [
    path('subir_img/', views.subir_img, name="subir_img"),
    path('mostrar_img/', views.mostrar, name="mostrar"),
    
]

