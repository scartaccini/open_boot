from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='inicio'),
    path('sumar_historia/', views.actualizar, name='actualiza'),
]
