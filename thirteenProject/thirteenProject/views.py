from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm 

####uso de widget(para poder personalizar los campos)
def widget(request):
    form_contacto=ContactForm()
    return render(request, "widget/form_widget.html",{"form_contacto":form_contacto})

