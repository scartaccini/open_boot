from django.contrib import messages
from django.shortcuts import render

def inicio(request):
    messages.add_message(request, messages.INFO, 'Le quedan 2 intentos más.')
    messages.success(request, 'es un mensaje flash! del tipo success')#otra forma
    return render(request,"index.html",{})

""" Para usar messages.debug en settings:
from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.DEBUG

messages.debug(request, 'Se ejecutaron las sentencias SQL.')
messages.info(request, 'Le quedan 2 intentos más.')
messages.success(request, 'El producto fue creado correctamente.')
messages.warning(request, 'Tu cuenta caduca en tres días.')
messages.error(request, 'Documento eliminado.')

"""