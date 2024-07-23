from django.shortcuts import get_object_or_404, render

from .models import Question

###otra forma
def detail(request, question_id):
    pregunta = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail2.html", {"pregunta": pregunta})