"""secondProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simplePlantilla/', views.simplePlantilla, name="simplePlantilla"),
    path('dinamicaPlantilla/<str:nombre>/', views.dinamicaPlantilla, name="dinamicaPlantilla"),
    path('dinamicaPlantilla2/<str:nombre>/', views.dinamicaPlantilla2, name="dinamicaPlantilla2"),
    path('dinamicaPlantilla3/', views.dinamicaPlantilla3, name="dinamicaPlantilla3"),
    path('comentarios/', views.comentarios, name="comentarios"),
    path('forloop/', views.forloop, name="forloop"),
    path('variable/', views.variableWith, name="variable"),
]
