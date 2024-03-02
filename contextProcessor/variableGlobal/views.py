from django.shortcuts import render

import datetime

def saludo(request):
    
    return render (request,"index.html",{})
