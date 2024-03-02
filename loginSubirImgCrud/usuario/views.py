from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from . forms import RegistroForm, ModDatosUsuForm
from django.urls import reverse_lazy
from django.contrib import messages
from blog.models import Post

class SignUpView(CreateView):
    model = User
    form_class = RegistroForm
    template_name = 'usuario/registrarUsuario.html'
    success_url = reverse_lazy('login')

class UpdatePassUsuario(UpdateView):
	model = User   
	form_class = ModDatosUsuForm
	template_name = 'usuario/modificar_datos_usu.html'
	success_url = reverse_lazy('login')

def inicio(request): 
    messages.success(request,"Listando todos los posts!")
    posts = Post.objects.all()

    return render(request,"blog/post_list.html",{'posteos':posts})
