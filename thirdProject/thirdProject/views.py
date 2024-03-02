from django.shortcuts import render

def estatico(request):
    context={}
    return render(request,"estatico.html",context)