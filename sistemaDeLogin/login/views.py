from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.models import User
from .forms import RegistroForm, ModDatosUsuForm
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def prueba(request):
    return render(request, 'prueba.html')

class SignUpView(CreateView):
    model = User
    form_class = RegistroForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class UpdatePassUsuario(UpdateView):
	model = User
    
	form_class = ModDatosUsuForm

	template_name = 'registration/modificar_datos_usu.html'

	success_url = reverse_lazy('login')