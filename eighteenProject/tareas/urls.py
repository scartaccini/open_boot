from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="tareas_index"),   
    path('crear_tarea/', views.crear_tarea, name="crear_tarea"),  
    path('detalle_tarea/<int:id>', views.detalle_tarea, name="detalle_tarea"),  
    path('editar_tarea/<int:id>', views.editar_tarea, name="editar_tarea"),  
    path('eliminar_tarea/<int:id>', views.eliminar_tarea, name="eliminar_tarea"),  
]