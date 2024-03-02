from django import forms
from django.forms import ModelForm, TextInput
from .models import Employee

class EmployeeForm(ModelForm):
    ##cuales son los campos del modelo que vamos a utilizar para manejar el formulario
    class Meta:
        model=Employee
        #fields='__all__' #muestra todos los campos
        #exclude=('email',) #muestra todos los campos menos email
        fields=['name','email']
        #extra_fields=['dir',]
        widgets= {'name': TextInput(attrs={'type':'text'})}
    
    ### para usar: en views.py : form_model=EmployeeForm(request.GET) o (request.POST)
    ### y controlar que sea valido: form_model.is_valid()
    def clean_name(self):
        name=self.cleaned_data.get("name") 
        if name != "open":
            raise forms.ValidationError("solo esta permitdo el nombre open")
        else:
            return name
