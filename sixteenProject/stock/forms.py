from django import forms
from django.forms import ModelForm,TextInput
from .models import Product


class ProductForm(ModelForm):
    name=forms.CharField(label="Nombre:",max_length=20, widget=TextInput(attrs={'class':'nombre'}))

    class Meta:
        model = Product
        fields = '__all__'
        ## OTRA FORMA , DE INCLUIR WIDGET
        #widgets= {'name': TextInput(attrs={'type':'text','class':'nombre'})}
