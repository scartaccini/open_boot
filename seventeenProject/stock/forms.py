from django import forms
#from django.forms import ModelForm
from .models import Product


class ProductForm(forms.ModelForm):
    #name=forms.CharField(label="Nombre:",max_length=20, widget=forms.TextInput(attrs={'class':'nombre'}))

    class Meta:
        model = Product
        fields = '__all__'