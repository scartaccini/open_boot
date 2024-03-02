from django import forms

class ContactForm(forms.Form):   
    name=forms.CharField(label="Nombre:", max_length=10, widget=forms.TextInput(attrs={'class':'input'}))
    email=forms.EmailField(label="Email:", max_length=50, widget=forms.EmailInput(attrs={'class':'email'}))
    msg=forms.CharField(label="Mensaje:", widget=forms.Textarea(attrs={'class':'msg'}))

    #####validaciones opcionales, personalizadas
    ##### primero pasa las validaciones de la clase(ejm max_length)
    ##### si pasa esas validaciones, controla validacion clean_
    def clean_name(self):
        name=self.cleaned_data.get("name") 
        if name != "open":
            raise forms.ValidationError("solo esta permitdo el valor open")
        else:
            return name


