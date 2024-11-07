from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import Question
from django.http import Http404
from django.views import generic
## defino lo que serían los controladores de la aplicación
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list} # le paso como contexto la variable latest_question_list
    return render(request, "polls/index.html", context) # renderiza la vista index.html con el contexto

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id) # obtengo la pregunta con el id pasado por parámetro
#     except Question.DoesNotExist: # si no existe la pregunta
#         raise Http404("Question does not exist")   # lanzo un error 404
#     return render(request, "polls/detail.html", {"question": question}) # renderizo la vista detail.html con el contexto de la pregunta

# Forma simplificada de detail:
def detail(request, question_id):
    # get_object_or_404 es una función que obtiene el objeto o lanza un error 404
    question = get_object_or_404(Question, pk=question_id) 
    return render(request, "polls/detail.html", {"question": question})

## Forma de hacerlo con vistas genéricas
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"



def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)