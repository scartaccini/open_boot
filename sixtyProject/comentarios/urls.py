from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name="test"),
    path('create/', views.create, name="create"),
    path('create2/', views.create2, name="create2"),
    path('delete/', views.delete, name="delete"),
    path('delete2/', views.delete2, name="delete2"),
]