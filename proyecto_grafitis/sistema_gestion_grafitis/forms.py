from django import forms

from .models import Grafiti


"""class ArtistaForm(forms.ModelForm):
    class Meta:
        model=Artista
        fields = [
            'name',
            'email',

        ]
        labels = {
			'name': 'Nombre',
			'email': 'Correo',
			
		}
        widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			
            # forms.Select(attrs={'class':'form-control'}),
			# forms.CheckboxSelectMultiple(),
		}
"""
class GrafitiForm(forms.ModelForm):
    class Meta:
        model=Grafiti
        #fields = '__all__'
        exclude=('user',)