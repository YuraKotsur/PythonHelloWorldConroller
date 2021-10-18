from django.shortcuts import render
from django.http import HttpResponse
from .models import NameFromUrl

# Create your views here.

def index(request):
    return HttpResponse('Hello World')

def return_var_from_url(request, name):
    saver = NameFromUrl(variable=name)
    saver.save()
    return HttpResponse(name)
