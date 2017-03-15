from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib.auth import authenticate
from .models import user_details

# Create your views here.
def transport_home(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(username=username, password=password)
    if user is None:
        raise Http404
    else :
        if user.is_active:
            
    return render(request, "home.html")
