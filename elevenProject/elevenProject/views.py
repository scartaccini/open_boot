from django.shortcuts import render
from django.http import HttpResponse

def form_get(request):
    return render(request,"forms/get/base.html", {})

def succes_get(request):
    if request.method == 'GET':
        contexto=request.GET["nombre"]
        return render(request,"forms/get/resultado.html",{"contexto":contexto})
#####################
def form_post(request):
    return render(request,"forms/post/base.html", {})
    
def success_post(request):
    if request.method == 'POST':
        contexto=request.POST["nombre"]
        return render(request,"forms/post/resultado.html",{"contexto":contexto})
        