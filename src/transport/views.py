from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import user_details
from .form import  LoginForm,RegistrationForm
# Create your views here.
#def login(request,template_name):

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            email=form.cleaned_data['email'])
            return HttpResponseRedirect('/')
        else:
            return render(request,'register.html',{'form':form})
    form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('register.html', variables)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")



