from django.http import HttpResponse
from django.shortcuts import render
from .models import Coment


def test(request):
    return HttpResponse("OK!!!")

def create(request):
    coment=Coment(name="Pablo",coment="esto es un comentario positivo")
    coment.save()
    return HttpResponse("Se creo comentario correctamente!")

#otra forma
def create2(request):
    coment=Coment.objects.create(name="Lucas",coment="esto es un comentario negativo")
    return HttpResponse("Se creo comentario correctamente!!!")

def delete(request):
    coment=Coment.objects.get(id=1)
    coment.delete()
    return HttpResponse("Se elimino comentario correctamente!")
#otra forma
def delete2(request):
    coment=Coment.objects.filter(id=2).delete()
    return HttpResponse("Se elimino comentario correctamente!!!")