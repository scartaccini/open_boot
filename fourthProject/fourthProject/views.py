from django.shortcuts import render

def herencia(request):
    context={}
    return render(request,"herencia.html",context)

def prueba(request):
    context={}
    return render(request,"prueba.html",context)

def ejemplo(request):
    context={}
    return render(request,"ejemplo.html",context)