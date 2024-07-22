from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from .models import Registro

@login_required #controla acceso
def inicio(request):
    registros = Registro.objects.all()
    return render(request,'index.html',{'registros':registros})

@login_required #controla acceso
#request.FILES porque recibe una imagen
def registrar(request):
    if request.method == "POST":
        form = RegistroForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})
