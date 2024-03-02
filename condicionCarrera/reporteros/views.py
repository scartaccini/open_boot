from django.shortcuts import render
from .models import Reporter
from .forms import ReporterForm
from django.db.models import F

def index(request):
    if request.method == "POST":
        form=ReporterForm(request.POST)
        if form.is_valid():
            form.save() #como se usa modelFom :ProductForm(request.POST)
            #form=ReporterForm() #sirve para limpiar los campos, porque los trae sin la respuesta
            
            return render(request, "home.html", {"form":form})
    else:
        form=ReporterForm()
        return render(request, "home.html", {"form":form})
    
def actualizar(request):    
    reporter = Reporter.objects.get(name="pepe") 
    reporter.stories_filed = F("stories_filed") + 1
    reporter.save()
    form=ReporterForm()
    return render(request, "home.html", {"form":form})
