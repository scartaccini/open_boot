from django.forms import ModelForm, DateInput
from .models import Tarea
from django import forms

class TareaForm(ModelForm):
    class Meta:
        model=Tarea
        #fields= '__all__'
        exclude=('fecha',)
        widgets= {'fecha_estimada': DateInput(attrs={'type':'date'})}
  