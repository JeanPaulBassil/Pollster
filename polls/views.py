from django.shortcuts import render

# Create your views here.
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context=context)

def detail(request, question_id):
    try:
        question = Question.object.get(pk=question_id)
    except Question.DoesNotExist: 
        raise Http404("Question does not exist")
    
    return render(request, 'polls/results.html', {'question': question})