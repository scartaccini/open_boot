from django.shortcuts import render
from .models import Reporter, Article
from django.http import HttpResponse
from datetime import date

def create(request):
    rep=Reporter(first_name="Pablo",last_name="Scartaccini",email="ps@gmail.com",address="Democracia 2008")
    rep.save()
    art1=Article(headline="Arranco el mundial!",publish=date(2022,11,27), reporter=rep)
    art1.save()
    art2=Article(headline="Todo esta caro!",publish=date(2022,11,22), reporter=rep)
    art2.save()
    art3=Article(headline="Bueno bueno",publish=date(2022,5,5), reporter=rep)
    art3.save()

    resultado= art2.reporter.last_name
    resultado_inverso= rep.article_set.all() #todos los articulos del reportero rep
    resultado_inverso_filtro= rep.article_set.filter(headline="Bueno bueno")#todos los articulos del reportero rep que tengana en headline="Bueno bueno"
    resultado_inverso_cantidad= rep.article_set.count()#cantidad de articulos del reportero rep

    return HttpResponse(resultado)