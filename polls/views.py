from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def streaming(request):
    #return render(request, 'polls/streaming.html', {'list_i': xrange(10000)}, stream=True)
    return render(request, 'polls/streaming.html', {'list_i': xrange(10000)})