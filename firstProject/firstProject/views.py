from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola")

def adios(request):
    return HttpResponse("Chau")

def adulto(request,edad):
    if edad >= 18:
        return HttpResponse("<h1>Eres mayor</h1>")
    else:
        return HttpResponse("No eres mayor")

def datos(request,edad,nombre):
    datos=["Tenes "," ", edad," ","y te llamas "," ", nombre]
    return HttpResponse(datos)

        