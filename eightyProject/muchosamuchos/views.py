from django.shortcuts import render
from .models import Publication, Note
from django.http import HttpResponse
from datetime import date

def create(request):
    pub1=Publication(title="Publicacion 1")
    pub1.save()
    pub2=Publication(title="Publicacion 2")
    pub2.save()
    pub3=Publication(title="Publicacion 3")
    pub3.save()
    pub4=Publication(title="Publicacion 4")
    pub4.save()
    pub5=Publication(title="Publicacion 5")
    pub5.save()
    pub6=Publication(title="Publicacion 6")
    pub6.save()
    pub7=Publication(title="Publicacion 7")
    pub7.save()

    note1=Note(headline="Nota 1")
    note1.save()
    note2=Note(headline="Nota 2")
    note2.save()
    note3=Note(headline="Nota 3")
    note3.save()
    note4=Note(headline="Nota 5")
    note4.save()
    note5=Note(headline="Nota 6")
    note5.save()
    note6=Note(headline="Nota 7")
    note6.save()
    note7=Note(headline="Nota 8")
    note7.save()
    
    note1.publications.add(pub1)
    note1.publications.add(pub2)
    note1.publications.add(pub3)
    note2.publications.add(pub4)
    note2.publications.add(pub5)
    note3.publications.add(pub6)
    note4.publications.add(pub7)
    note4.publications.add(pub7)
    note5.publications.add(pub7)
    note6.publications.add(pub7)
    note6.publications.add(pub7)

    #note1.publications.remove(pub1) remueve pub1 de note1

    resultado2=Publication.objects.get(id=5)
    resultado2=resultado2.note_set.all()

    resultado= note1.publications.all()
    return HttpResponse(resultado2)
    #return HttpResponse(resultado)