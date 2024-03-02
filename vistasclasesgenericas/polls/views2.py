from django.shortcuts import get_object_or_404, render

from .models import Question

###otra forma
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail2.html", {"question": question})