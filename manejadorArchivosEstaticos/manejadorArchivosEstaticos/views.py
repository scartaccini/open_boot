from django.shortcuts import render

def probar(request):
    return render(request,"prueba.html",{})