from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="agenda_index"),        
    path('<str:letra>', views.index, name="agenda_index"),  
    ###la vista index tiene dos path porque se le puede o no pasar un parametro
    ###En el archivo agenda/letras.html se le pasa un parametro para que busque por una letra
    path('crear_contacto/', views.crear_contacto, name="crear_contacto"),  
    path('detalle_contacto/<int:id>', views.detalle_contacto, name="detalle_contacto"),  
    path('editar_contacto/<int:id>', views.editar_contacto, name="editar_contacto"),  
    path('eliminar_contacto/<int:id>', views.eliminar_contacto, name="eliminar_contacto"),  
]