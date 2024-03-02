from django.shortcuts import render, redirect
from .models import Producto
from .carro import Carro
from django.core.mail import EmailMessage

def home(request):
    #carro=Carro(request) si usamos sistema de login 
    return render(request,'home.html',{})


def tienda(request):    
    
    #carro=Carro(request) si usamos sistema de login 
    productos=Producto.objects.all()

    return render(request, "tienda.html", {"productos":productos})

def agregar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)

    return redirect("inicio")


def eliminar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("inicio")


def restar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return redirect("inicio")


def limpiar_carro(request, producto_id):

    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("inicio")

def compra(request):
    carro=Carro(request)
    nombre_articulo = {}
    cantidad = {}
    precio = {}
    for key, value in carro.carro.items():
        nombre_articulo[key] = value["nombre"]
        cantidad[key] = value["cantidad"]
        precio[key] = value["precio"]        

    valor1=nombre_articulo.values()
    valor2=cantidad.values()
    valor3=precio.values()    
    
    email=EmailMessage("Detalles de su compra: ",
            "Producto {} cantidad {} precio:\n\n {}".format(valor1,valor2,valor3),
            "",["montevideobits@gmail.com"],reply_to=[""])
    try:
        email.send()
        carro.limpiar_carro()
        return render(request,"compra.html",{})
    except:
        return render(request,"compra_fallida.html",{})
    
    
    