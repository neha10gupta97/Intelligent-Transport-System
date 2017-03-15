from django.shortcuts import render
from django.http import HttpResponse
from .models import user

# Create your views here.
def transport_home(request):
    return render(request, "home.html")
