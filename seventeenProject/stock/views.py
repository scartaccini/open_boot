from django.shortcuts import render
from .forms import ProductForm

def index(request):
    if request.method == "POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save() #como se usa modelFom :ProductForm(request.POST)
            form=ProductForm() #sirve para limpiar los campos, porque los trae sin la respuesta
            return render(request, "stock/index.html", {"form":form})
    else:
        form=ProductForm()
        return render(request, "stock/index.html", {"form":form})