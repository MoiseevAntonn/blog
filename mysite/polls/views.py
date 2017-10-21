from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Question
from django.shortcuts import render
# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': question_list}
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not excist')
    return render(request,'polls/detail.html',{'question':question})

def result(request,question_id):
    responce = "You are looking results of %s"
    return HttpResponse(responce % question_id)

def vote(request,question_id):
    responce = "you are voting for question %s"
    return HttpResponse(responce % question_id)