from django.http import Http404
from django.shortcuts import render
from .models import Question

def index(request):
    list_question = Question.objects.all()
    return render(request, "polls/index.html", {"list_question": list_question})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})