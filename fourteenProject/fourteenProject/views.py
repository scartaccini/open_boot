from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm 

####uso de validacion
def validacion(request):
    if request.method == 'POST':
        contexto=ContactForm(request.POST)
        if contexto.is_valid(): ####uso de validacion de la clase(ejm max_length), si pasa, controla validacion clean_
            return HttpResponse("VALIDO")
        else:
            return render(request,"validez.html",{"contexto":contexto})
        
    contexto=ContactForm()
    return render(request,"validez.html",{"contexto":contexto})