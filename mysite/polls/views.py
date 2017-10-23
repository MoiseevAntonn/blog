
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': question_list}
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    return render(request,'polls/detail.html',{'question': question})

def result(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request, 'polls/result.html',{'question': question})

def votes(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{'question': question,'error_message':'You didnt select a choise'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question_id)))