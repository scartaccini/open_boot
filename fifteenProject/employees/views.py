from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm

def index(request):
    form_model=EmployeeForm()
    return render(request,"employees/index.html",{"form_model":form_model})

''' hace uso del control, def clean_name(self):
def index(request):
    form_model=EmployeeForm(request.GET)
    return render(request,"employees/index.html",{"form_model":form_model})'''

""" con manejo de validacion, def clean_name
def index(request):
    form_model=EmployeeForm(request.GET)
    if form_model.is_valid():
        return HttpResponse("DAtos validos")
    return render(request,"employees/index.html",{"form_model":form_model})

"""