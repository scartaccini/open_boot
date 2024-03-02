from django.shortcuts import render
from django.http import HttpResponse
from .forms import ComentForm 

def form_get(request):
    coment_form=ComentForm()
    return render(request,"get/form.html", {"coment_form":coment_form})

def resultado_get(request):
    if request.method != 'GET':
        return HttpResponse("metodo no permitido")
    contexto=request.GET['name']
    return render(request,"get/resultado.html",{"contexto":contexto})
#####################
def form_post(request):
    coment_form=ComentForm()
    return render(request,"post/form.html", {"coment_form":coment_form})

def resultado_post(request):
    if request.method != 'POST':
        return HttpResponse("metodo no permitido")
    contexto=request.POST['name']
    return render(request,"post/resultado.html",{"contexto":contexto})
#####################
def form_precargado(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['name'])
    coment_form=ComentForm({"name":"Pablo","url":"http://www.ps.com","coment":"hola que tal!"})
    return render(request,"precargado/form.html",{"coment_form":coment_form})