from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Entry

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

def eliminar_autor(request):
    autor=Author.objects.get(id=14)
    autor.delete()
    return HttpResponse("Se elimino autor correctamente!")

def actualizacion_entry(request):
    entrada=Entry.objects.get(id=10)
    entrada.author=Author.objects.get(id=2)
    entrada.headline="historia d l manya"
    entrada.body_text="nace en 18912, seras eterno como el tiempo y floreceras en cada primavera"
    entrada.rating = 3
    entrada.save()
    return HttpResponse("Entrada modificada correctamente!")

def mostrar_entradas(request):
    entradas=Entry.objects.all()
    return render(request, "posts/entradas.html",{"entradas":entradas})

def crear_entrada(request):
    entrada=Entry(author=Author.objects.get(id=3),headline="Prueba!!",body_text="esto es un comentario positivo", rating=2)
    entrada.save()
    return HttpResponse("Se creo entrada correctamente!")

def eliminarEntrada(request):
    entrada=Entry.objects.get(id=1)
    entrada.delete()
    return HttpResponse("Se elimino entrada correctamente!")
