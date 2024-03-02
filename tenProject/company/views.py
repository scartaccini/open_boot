from django.shortcuts import render
from django.http import HttpResponse
from .models import Salary, Country, Location, Place, Job, Employee

################### SALARIO - SALARY
def crear_salario(request,nivel):
    if nivel == 1:
        salario=Salary(amount=30000,extra_dec=True, extra_jun=True)
    elif nivel == 2:
        salario=Salary(amount=60000,extra_dec=True, extra_jun=True)
    elif nivel == 3:
        salario=Salary(amount=105000,extra_dec=False, extra_jun=False)
    else:    
        return HttpResponse("No existe ese nivel de salario!")    
    salario.save()

    return HttpResponse("Se creo salario correctamente!")

def eliminar_salario_id(request,identificador):
    salario=Salary.objects.filter(id=identificador)
    if salario: 
        salario.delete()
        return HttpResponse("Se elimino salario correctamente!")
    else:
        return HttpResponse("No existe salario con ese id!")

def eliminar_salario_monto(request,monto):
    salario=Salary.objects.filter(amount=monto)
    if not salario:
        return HttpResponse("No existe ese monto de salario!")
    salario.delete()
    return HttpResponse("Salario/s eliminado/s correctamente!")

def actualizar_salario_monto(request,monto,monto_actualizado):
    salario=Salary.objects.filter(amount=monto)
    if salario:
        for s in salario:
            s.amount=monto_actualizado
            s.save()
    else:
        return HttpResponse("No existe el monto a modificar!")
    return HttpResponse("Salario modificado correctamente!")

def actualizar_salario_id(request,identificador,monto_actualizado):
    salario=Salary.objects.get(id=identificador)
    salario.amount=monto_actualizado
    salario.save()
    return HttpResponse("Salario modificado correctamente!")
    
def listar_salario(request):
    lista_salario=Salary.objects.all()
    return render(request, "company/salary/lista_salario.html",{"lista_salario":lista_salario})   

def listar_salario_id(request,identificador):
    salario=Salary.objects.filter(id=identificador)
    if salario:
        return render(request, "company/salary/lista_salario_id.html",{"salario":salario}) 
    return HttpResponse("No existe salario con ese id!")    
################### PAIS - COUNTRY
def crear_pais(request,pais):
    pais=Country(name=pais.upper()) 
    pais.save()
    return HttpResponse("Se creo pais correctamente!")

def listar_pais(request):
    listar_pais=Country.objects.all()
    return render(request, "company/country/lista_pais.html",{"listar_pais":listar_pais}) 
    
def eliminar_pais(request,pais):
    pais=Country.objects.filter(name=pais.upper())
    if pais:
        pais.delete()
        return HttpResponse("Se elimino pais correctamente!")
    else:
        return HttpResponse("No existe pais con ese nombre!") 

def eliminar_pais_id(request,identificador):
    pais=Country.objects.filter(id=identificador)
    if pais:
        pais.delete()
        return HttpResponse("Se elimino pais correctamente!")
    else:
        return HttpResponse("No existe pais con ese id!") 
################### BARRIO - lOCATION
def crear_barrio(request,barrio,pais):
    country=Country.objects.get(name=pais.upper())
    barrio=Location(name=barrio.upper(),country=country)
    barrio.save()
    return HttpResponse("Se creo barrio correctamente!")

def listar_barrio(request):
    lista_barrio=Location.objects.all()
    return render(request, "company/location/lista_barrio.html",{"lista_barrio":lista_barrio})  

def listar_barrio_pais(request,pais):
    country=Country.objects.filter(name=pais.upper())
    lista_barrio_pais=Location.objects.filter(country=country[0])
    return render(request, "company/location/lista_barrio_pais.html",{"lista_barrio_pais":lista_barrio_pais}) 
  
def listar_barrio_idpais(request,idpais):    
    country=Country.objects.get(id=idpais)
    lista_barrio_idpais=Location.objects.filter(country=country)
    return render(request, "company/location/lista_barrio_idpais.html",{"lista_barrio_idpais":lista_barrio_idpais}) 

def eliminar_barrio(request,barrio):
    barrio=Location.objects.filter(name=barrio.upper())
    if barrio:
        barrio.delete()
        return HttpResponse("Se elimino barrio correctamente!")
    else:
        return HttpResponse("No existe barrio con ese nombre!")

def eliminar_barrio_id(request,identificador):
        barrio=Location.objects.filter(id=identificador)
        if barrio:
            barrio.delete()
            return HttpResponse("Se elimino barrio correctamente!")
        else:
            return HttpResponse("No existe barrio con ese id!") 
################### LUGAR - PLACE
def crear_lugar(request,nombre,dir,zip,barrio):
    location=Location.objects.get(name=barrio.upper())
    lugar=Place(name=nombre.upper(),address=dir.upper(),zip=zip,location=location)
    lugar.save()
    return HttpResponse("Se creo lugar correctamente!")

def listar_lugar(request):
    lista_lugar=Place.objects.all()
    return render(request, "company/place/lista_lugar.html",{"lista_lugar":lista_lugar})  

def listar_lugar_barrio(request,barrio):
    lista_barrio=Location.objects.filter(name=barrio.upper())
    #print(lista_barrio)
    #print(lista_barrio[0])#    
    lista_lugar_barrio=Place.objects.filter(location=lista_barrio[0])
    return render(request, "company/place/lista_lugar_barrio.html",{"lista_lugar_barrio":lista_lugar_barrio}) 
 
def listar_lugar_barrio_id(request,identificador):
    lista_barrio=Location.objects.get(id=identificador)
    lista_lugar_barrio_id=Place.objects.filter(location=lista_barrio)
    return render(request, "company/place/lista_lugar_barrio_id.html",{"lista_lugar_barrio_id":lista_lugar_barrio_id})

def eliminar_lugar(request,lugar):
    lugar=Place.objects.filter(name=lugar.upper())
    if lugar:
        lugar.delete()
        return HttpResponse("Se elimino lugar correctamente!")
    return HttpResponse("No existe lugar con ese nombre!")

def eliminar_lugar_id(request,identificador):
    lugar=Place.objects.filter(id=identificador)
    if lugar:
        lugar.delete()
        return HttpResponse("Se elimino lugar correctamente!")
    return HttpResponse("No existe lugar con ese nombre!")

def actualizar_lugar(request,nombre,dir,zip,barrio):
    lugar=Place.objects.get(name=nombre.upper())
    lugar.address=dir.upper()
    lugar.zip=zip.upper()
    location=Location.objects.get(name=barrio.upper())
    lugar.location=location
    lugar.save()
    return HttpResponse("Lugar modificado correctamente!")    
################### TRABAJO - JOB
def crear_trabajo(request,titulo,comentario,salario):
    salario=Salary.objects.get(amount=salario)
    trabajo=Job(title=titulo.upper(),description=comentario.upper(),salary=salario)
    trabajo.save()
    return HttpResponse("Se creo trabajo correctamente!")

def crear_trabajo_id(request,identificador,titulo,comentario):
    salario=Salary.objects.get(id=identificador)
    trabajo=Job(title=titulo.upper(),description=comentario.upper(),salary=salario)
    trabajo.save()
    return HttpResponse("Se creo trabajo correctamente!")    
    
def listar_trabajo(request):
    lista_trabajo=Job.objects.all()
    return render(request, "company/job/lista_trabajo.html",{"lista_trabajo":lista_trabajo})  

def listar_trabajo_id_salario(request,identificador):
    salario=Salary.objects.get(id=identificador)
    lista_trabajo_id_salario=Job.objects.filter(salary=salario)
    return render(request, "company/job/lista_trabajo_id_salario.html",{"lista_trabajo_id_salario":lista_trabajo_id_salario})

def eliminar_trabajo(request,titulo):
    trabajo=Job.objects.filter(title=titulo.upper())
    trabajo.delete()
    return HttpResponse("Se elimino trabajo correctamente!")

def eliminar_trabajo_id(request,identificador):
    trabajo=Job.objects.get(id=identificador)
    trabajo.delete()
    return HttpResponse("Se elimino trabajo correctamente!")

def actualizar_trabajo(request,titulo,descripcion,salario):       
    trabajo=Job.objects.get(title=titulo.upper())
    trabajo.description=descripcion.upper()
    salario=Salary.objects.get(amount=salario)
    trabajo.salary=salario
    trabajo.save()
    return HttpResponse("Trabajo modificado correctamente!")    

def actualizar_trabajo_id(request,identificador_trabajo,identificador_salario,titulo,descripcion):       
    trabajo=Job.objects.get(id=identificador_trabajo)
    salario=Salary.objects.get(id=identificador_salario)
    trabajo.title=titulo.upper()
    trabajo.description=descripcion.upper()
    trabajo.salary=salario
    trabajo.save()
    return HttpResponse("Trabajo modificado correctamente!")  
################### EMPLEADO - EMPLOYEE
def crear_empleado(request,nombre,apellido,email,dir,id_trabajo,id_lugar):
    trabajo=Job.objects.get(id=id_trabajo)
    lugar=Place.objects.get(id=id_lugar)
    empleado=Employee(name=nombre.upper(),last_name=apellido.upper(),email=email.upper(),address=dir.upper(),job=trabajo,place=lugar)
    empleado.save()
    return HttpResponse("Se creo empleado correctamente!") 

def listar_empleado(request):
    lista_empleado=Employee.objects.all()
    return render(request, "company/employee/lista_empleado.html",{"lista_empleado":lista_empleado}) 

def listar_empleado_id_trabajo(request,identificador):
    trabajo=Job.objects.get(id=identificador)
    lista_empleado_id_trabajo=Employee.objects.filter(job=trabajo)
    return render(request, "company/employee/lista_empleado_id_trabajo.html",{"lista_empleado_id_trabajo":lista_empleado_id_trabajo})

def listar_empleado_id_lugar(request,identificador):
    lugar=Place.objects.get(id=identificador)
    lista_empleado_id_lugar=Employee.objects.filter(place=lugar)
    return render(request, "company/employee/lista_empleado_id_lugar.html",{"lista_empleado_id_lugar":lista_empleado_id_lugar})

def eliminar_empleado_id(request,identificador):
    empleado=Employee.objects.get(id=identificador)
    empleado.delete()
    return HttpResponse("Se elimino empleado correctamente!")

def actualizar_empleado_id(request,identificador,identificador_trabajo,identificador_lugar,nombre,apellido,email,dir):       
    empleado=Employee.objects.get(id=identificador)
    trabajo=Job.objects.get(id=identificador_trabajo)
    lugar=Place.objects.get(id=identificador_lugar)
    empleado.name=nombre.upper()
    empleado.last_name=apellido.upper()
    empleado.email=email.upper()
    empleado.address=dir.upper()
    empleado.job=trabajo
    empleado.place=lugar
    empleado.save()
    return HttpResponse("Empleado modificado correctamente!")  