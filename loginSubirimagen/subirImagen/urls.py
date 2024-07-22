from django.urls import path
from .views import inicio,registrar

urlpatterns = [
    path('', inicio, name='index'),  
    path('registar', registrar, name='registrar'),    
]
