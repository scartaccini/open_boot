"""TwelveProject URL Configuration

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
    path('form_get/', views.form_get, name="form_get"),
    path('resultado_get/', views.resultado_get, name="resultado_get"),

    path('form_post/', views.form_post, name="form_post"),
    path('resultado_post/', views.resultado_post, name="resultado_post"),

    path('form_precargado/', views.form_precargado, name="form_precargado"),
]
