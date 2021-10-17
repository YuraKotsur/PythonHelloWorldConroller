from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World')

def return_var_from_url(request, name):
    return HttpResponse(name)
