from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('crear_salario/<int:nivel>/', views.crear_salario, name="crear_salario"),
    path('eliminar_salario_id/<int:identificador>/', views.eliminar_salario_id, name="eliminar_salario_id"),
    path('eliminar_salario_monto/<int:monto>/', views.eliminar_salario_monto, name="eliminar_salario_monto"),
    path('actualizar_salario_monto/<int:monto>/<int:monto_actualizado>/', views.actualizar_salario_monto, name="actualizar_salario_monto"),
    path('actualizar_salario_id/<int:identificador>/<int:monto_actualizado>/', views.actualizar_salario_id, name="actualizar_salario_id"),
    path('listar_salario/', views.listar_salario, name="listar_salario"),  
    path('listar_salario_id/<int:identificador>/', views.listar_salario_id, name="listar_salario_id"),
    #########
    path('crear_pais/<str:pais>/', views.crear_pais, name="crear_pais"),        
    path('listar_pais/', views.listar_pais, name="listar_pais"),  
    path('eliminar_pais/<str:pais>/', views.eliminar_pais, name="eliminar_pais"),
    path('eliminar_pais_id/<int:identificador>/', views.eliminar_pais_id, name="eliminar_pais_id"),
    #########
    path('crear_barrio/<str:barrio>/<str:pais>/', views.crear_barrio, name="crear_barrio"),  
    path('listar_barrio/', views.listar_barrio, name="listar_barrio"), 
    path('listar_barrio_pais/<str:pais>/', views.listar_barrio_pais, name="listar_barrio_pais"),
    path('listar_barrio_idpais/<int:idpais>/', views.listar_barrio_idpais, name="listar_barrio_idpais"),
    path('eliminar_barrio/<str:barrio>/', views.eliminar_barrio, name="eliminar_barrio"), 
    path('eliminar_barrio_id/<int:identificador>/', views.eliminar_barrio_id, name="eliminar_barrio_id"), 
    #########
    path('crear_lugar/<str:nombre>/<str:dir>/<str:zip>/<str:barrio>/', views.crear_lugar, name="crear_lugar"),
    path('listar_lugar/', views.listar_lugar, name="listar_lugar"),      
    path('listar_lugar_barrio/<str:barrio>/', views.listar_lugar_barrio, name="listar_lugar_barrio"),  
    path('listar_lugar_barrio_id/<int:identificador>/', views.listar_lugar_barrio_id, name="listar_lugar_barrio_id"), 
    path('eliminar_lugar/<str:lugar>/', views.eliminar_lugar, name="eliminar_lugar"), 
    path('eliminar_lugar_id/<int:identificador>/', views.eliminar_lugar_id, name="eliminar_lugar_id"), 
    path('actualizar_lugar/<str:nombre>/<str:dir>/<str:zip>/<str:barrio>/', views.actualizar_lugar, name="actualizar_lugar"), 
    #########
    path('crear_trabajo/<str:titulo>/<str:comentario>/<int:salario>/', views.crear_trabajo, name="crear_trabajo"),
    path('crear_trabajo_id/<int:identificador>/<str:titulo>/<str:comentario>/', views.crear_trabajo_id, name="crear_trabajo_id"),
    path('listar_trabajo/', views.listar_trabajo, name="listar_trabajo"),   
    path('listar_trabajo_id_salario/<int:identificador>/', views.listar_trabajo_id_salario, name="listar_trabajo_id_salario"),
    path('eliminar_trabajo/<str:titulo>/', views.eliminar_trabajo, name="eliminar_trabajo"), 
    path('eliminar_trabajo_id/<int:identificador>/', views.eliminar_trabajo_id, name="eliminar_trabajo_id"),   
    path('actualizar_trabajo/<str:titulo>/<str:descripcion>/<str:salario>/', views.actualizar_trabajo, name="actualizar_trabajo"), 
    path('actualizar_trabajo_id/<int:identificador_trabajo>/<int:identificador_salario>/<str:titulo>/<str:descripcion>/', views.actualizar_trabajo_id, name="actualizar_trabajo_id"),
    ##########
    path('crear_empleado/<str:nombre>/<str:apellido>/<str:email>/<str:dir>/<int:id_trabajo>/<int:id_lugar>/', views.crear_empleado, name="crear_empleado"),
    path('listar_empleado/', views.listar_empleado, name="listar_empleado"),     
    path('listar_empleado_id_trabajo/<int:identificador>/', views.listar_empleado_id_trabajo, name="listar_empleado_id_trabajo"),
    path('eliminar_empleado_id/<int:identificador>/', views.eliminar_empleado_id, name="eliminar_empleado_id"),     
    path('actualizar_empleado_id/<int:identificador>/<int:identificador_trabajo>/<int:identificador_lugar>/<str:nombre>/<str:apellido>/<str:email>/<str:dir>/', views.actualizar_empleado_id, name="actualizar_empleado_id"),

]