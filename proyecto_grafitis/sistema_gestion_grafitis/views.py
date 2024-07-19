from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from.models import Grafiti
from .forms import GrafitiForm

@login_required
def index(request):
    #lista_artistas=Artista.objects.all() lista todos los artistas
    #lista a todos los usaurios
    #user = get_user_model() 
    #lista_usuarios=user.objects.all()
    #lista todos los grafitis del artista con id 1
    #lista_usuarios=Grafiti.objects.filter(artista_id=1)
    lista_grafitis=Grafiti.objects.all()
    #return render(request, "inicio.html",{"lista_artistas":lista_artistas, "lista_grafitis":lista_grafitis,"lista_usuarios":lista_usuarios}) 
    return render(request, "index.html",{"lista_grafitis":lista_grafitis}) 

@login_required
def crea_grafiti(request):
    if request.method == 'POST':
        form = GrafitiForm(request.POST, request.FILES)       
        if form.is_valid():
            grafiti = form.save(commit=False)#no hace commit porque falta pasarle a grafiti el user, que es el usuario
            #print(request.POST['name'])
            grafiti.user = request.user
            form.save()
            return redirect(index)         
    else:
        form=GrafitiForm()
        return render(request,"crearGrafiti.html",{'form':form})
    
@login_required
#request.FILES porque recibe una imagen
def edita_grafiti(request, id_grafiti):
    #grafiti= Grafiti.objects.get(pk=id_grafiti)
    grafiti = get_object_or_404(Grafiti, pk=id_grafiti)
    if request.method == "POST":
        form = GrafitiForm(request.POST,request.FILES, instance=grafiti)
        if form.is_valid():
            grafiti = form.save(commit=False)
            #print(request.POST['name'])
            grafiti.user = request.user
            grafiti.save()
            return redirect('index')
            #return redirect('index', id_grafiti=grafiti.id)
    else:
        form = GrafitiForm(instance=grafiti)
        usu = grafiti.user.username
    return render(request, 'editar_grafiti.html', {'form': form, 'usu':usu})

@login_required
def elimina_grafiti(request,id_grafiti):
    grafiti = get_object_or_404(Grafiti, pk=id_grafiti)
    #grafiti= Grafiti.objects.get(pk=id_grafiti)
    if request.method == "POST":
        #form = GrafitiForm(request.POST,request.FILES)
        if grafiti:
            
            grafiti.delete()
            return redirect('index')
            #return redirect('inicio', id_grafiti=grafiti.id)
    else:
        
        nombre = grafiti.name
        usu = grafiti.user.username
    return render(request, 'eliminar_grafiti.html', {'usu':usu, 'nombre':nombre})

@login_required
def busca_grafiti(request):
    if request.method == 'GET':
        if request.GET.get('search','') == "":
            
            form={}
            return render(request,"buscar_grafiti.html",{"form":form})
        #print("primer valor cuando entra:",request.GET.get('search',''))
        # request.GET.get('search','') la primera vez no se presiona el btn search, entonces trae todo 
        # porque busca por vacio ''
        # cuando se toca el btn search ahi se busca por lo que se puso en el campo de buscar
        form=Grafiti.objects.filter(name__istartswith=request.GET.get('search',''))   
            
        return render(request,"buscar_grafiti.html",{"form":form})
    #form=Grafiti.objects.all()
    #return render(request,"index.html",{"form":form})
