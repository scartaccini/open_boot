from django import forms

class ComentForm(forms.Form):
    name=forms.CharField(label="Escribe tu nombre", max_length=50, help_text="maximo 50 caracteres")
    url=forms.URLField(label="tu sitio web" ,initial="http://www.",required=False)
    coment=forms.CharField()