from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Agenda
from .forms import AgendaForm
from django.contrib import messages

def index(request,letra=None):
    if letra != None:
        form=Agenda.objects.filter(nombre__istartswith=letra)
        return render(request,"./agenda/index.html",{"form":form})
    if request.method == 'GET':
        form=Agenda.objects.filter(nombre__contains=request.GET.get('search',''))
        #form=Agenda.objects.filter(nombre__contains=request.GET["search",""])
        return render(request,"./agenda/index.html",{"form":form})
    form=Agenda.objects.all()
    return render(request,"./agenda/index.html",{"form":form})
    

def crear_contacto(request):
    if request.method == "POST":
        form=AgendaForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Contacto creado')   
            return redirect("agenda_index")
    else:
        form=AgendaForm()
        return render(request, "agenda/crear.html", {"form":form})

def detalle_contacto(request, id):
    form=Agenda.objects.get(id=id)
    return render(request, "agenda/detalle.html", {"form":form})

def editar_contacto(request, id):
    contacto=Agenda.objects.get(id=id)
    if request.method == "POST":        
        form=AgendaForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Contacto actualizado')         
            form=Agenda.objects.all()
            return render(request, "agenda/index.html", {"form":form}) 
    else:
        #form=AgendaForm(initial={"id":contacto.id,"nombre":contacto.nombre, "apellido":contacto.apellido})
        #otra forma:
        form=AgendaForm(instance=contacto)
        return render(request, "agenda/crear.html", {"form":form})

def eliminar_contacto(request,id):
    contacto=Agenda.objects.get(id=id)
    contacto.delete()
    messages.success(request, 'Contacto eliminado')   
    return redirect("agenda_index")