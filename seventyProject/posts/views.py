from django.http import HttpResponse
from django.shortcuts import render
from .models import Author

def autores(request):
    authors=Author.objects.all()
    #autordenados=Author.objects.all().order_by("email")
    #id_menores_de_5=Author.objects.filter(id__lt=5) #__gt,__lte,__gte,__contains,__exact,__inexact
    #Author.objects.filter(email__contains="@example.com")
    return render(request, "posts/autores.html",{"authors":authors})

def autor(request):
    filtered=Author.objects.filter(email="jesse52@example.com")
    return render(request, "posts/autor.html",{"filtered":filtered})

def autor_id(request):
    id=Author.objects.get(id=1)
    return render(request, "posts/autor_id.html",{"id":id})
    
def autores_limite(request):
    authors=Author.objects.all()[:3]
    return render(request, "posts/autores_limite.html",{"authors":authors})
    
def actualizacion(request):
    autor=Author.objects.get(id=1)
    autor.name="PEPE"
    autor.email="pepe@gmail.com"
    autor.save()
    return HttpResponse("Autor modificado correctamente!")