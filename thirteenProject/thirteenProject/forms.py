from django import forms

class ContactForm(forms.Form):   
    name=forms.CharField(label="Nombre:", max_length=50, widget=forms.TextInput(attrs={'class':'input'}))
    email=forms.EmailField(label="Email:", max_length=50, widget=forms.EmailInput(attrs={'class':'email'}))
    msg=forms.CharField(label="Mensaje:", widget=forms.Textarea(attrs={'class':'msg'}))