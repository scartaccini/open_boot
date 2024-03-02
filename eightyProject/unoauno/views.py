from django.shortcuts import render
from .models import Place, Restaurant
from django.http import HttpResponse

def create(reuest):
    dominos=Place(name="Dominos",address="Av italia 333")
    dominos.save()
    restaurante=Restaurant(numbre_of_employees=25, place=dominos)
    restaurante.save()
 
    return HttpResponse(restaurante.place.name)
