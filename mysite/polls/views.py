
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import Question,Choice
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.core.paginator import Paginator



# Create your views here.
def index(request,page_number = 1):
    question_list = Question.objects.all()
    current_list = Paginator(question_list,4)
    return render(request,'polls/index.html',{'latest_question_list':current_list.page(page_number),'username':auth.get_user(request).username})


def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not excist')
    return render(request,'polls/detail.html',{'question':question})

def result(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'polls/result.html',{'question':question})



def votes(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{'question': question,'error_message':'You didnt select a choise'})
    else:
        if "test" not in request.session:
            selected_choice.votes += 1
            selected_choice.save()
            request.session.set_expiry(60)
            request.session['test'] = True
        return HttpResponseRedirect('/polls/'+str(question_id)+'/results/')