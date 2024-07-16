from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def simplePlantilla(request):
    return render(request,"simplePlantilla.html",{})

def comentarios(request):
    categorias=["Mozo","Cajero","Cheff"]
    context={"categorias":categorias}
    return render(request, "comentarios.html",context)

def forloop(request):
    categorias=["Mozo","Cajero","Cheff"]
    context={"categorias":categorias}
    return render(request, "accionesEnLista.html",context)

def dinamicaPlantilla(request,nombre):
    context={"nombre":nombre}
    return render(request,"dinamicaPlantilla.html",context)


def dinamicaPlantilla2(request,nombre):
    categorias=["Mozo","Cajero","Cheff"]
    context={"nombre":nombre,"categorias":categorias}
    return render(request,"dinamicaPlantilla.html",context)

def dinamicaPlantilla3(request):
  categorias=["Mozo","Cajero","Cheff"] 
  template = loader.get_template('dinamicaConCargador.html')
  context = {
    'categorias': categorias,
  }
  return HttpResponse(template.render(context, request))