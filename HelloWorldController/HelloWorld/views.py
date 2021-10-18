from django.shortcuts import render
from django.http import HttpResponse
from .models import NameFromUrl

# Create your views here.

def index(request):
    return HttpResponse('Hello World')

def saveNameToDb(string):
    saver = NameFromUrl(variable=string)
    saver.save()


def return_var_from_url(request, name):
    saveNameToDb(name)
    return HttpResponse(name)
