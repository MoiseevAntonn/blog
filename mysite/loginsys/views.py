

# Create your
#
#  views here.
from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm





def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password )
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            args['login_error'] = "bred"
            return render_to_response('loginsys/login.html',args)
    else:
            return render_to_response('loginsys/login.html',args)



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('polls:index'))

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username = new_user_form.cleaned_data['username'], password = new_user_form.cleaned_data['password1'])
            auth.login(request,new_user)
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            args['form'] = new_user_form
    return render(request,"loginsys/register.html",args)
