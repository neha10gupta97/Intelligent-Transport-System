from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import user_details
from .form import  LoginForm
# Create your views here.
def login(request,template_name):
    # if request.method=='post':
    #     session.pop('user', None)
    username = request.POST.get('username','admin')
    password = request.POST.get('password','admin')
    user = authenticate(username=username, password=password)
    form = LoginForm(request.POST)
    if form.is_valid():
        messages.success(request, "Successsfully Created")
    if user is None:
        raise Http404
    else :
        if user.is_authenticated():
            return HttpResponseRedirect('/home')

    return render(request, "login.html")

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")

