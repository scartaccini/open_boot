from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarea
from .forms import TareaForm
from django.contrib import messages

def index(request):
    if request.method == 'GET':
        #print("primer valor cuando entra:",request.GET.get('search',''))
        # request.GET.get('search','') la primera vez no se presiona el btn search, entonces trae todo 
        # porque busca por vacio ''
        # cuando se toca el btn search ahi se busca por lo que se puso en el campo de buscar
        form=Tarea.objects.filter(titulo__contains=request.GET.get('search',''))        
        return render(request,"./tareas/index.html",{"form":form})
    #form=Tarea.objects.all()
    #return render(request,"./tareas/index.html",{"form":form})
   
def crear_tarea(request):
    if request.method == "POST":
        form=TareaForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Tarea creada')   
            return redirect("tareas_index")
    else:
        form=TareaForm()
        return render(request, "tareas/crear.html", {"form":form})

def detalle_tarea(request,id):
    form=Tarea.objects.get(id=id)
    return render(request, "tareas/detalle.html", {"form":form})

def editar_tarea(request,id):
    tarea=Tarea.objects.get(id=id)
    if request.method == "POST":        
        form=TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Tarea actualizada')         
            form=Tarea.objects.all()
            return render(request, "tareas/index.html", {"form":form}) 
    else:
        #form=TareaForm(initial={"id":tarea.id,"titulo":tarea.titulo, "descripcion":tarea.descripcion})
        #otra forma:
        form=TareaForm(instance=tarea)
        return render(request, "tareas/crear.html", {"form":form})

def eliminar_tarea(request,id):
    tarea=Tarea.objects.get(id=id)
    tarea.delete()
    messages.success(request, 'Tarea eliminada')   
    return redirect("tareas_index")