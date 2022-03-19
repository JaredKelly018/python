from django.shortcuts import render
from django.http import HttpResponse

 # Create your views here.

def index(request):
 return HttpResponse('Hello!')

def rin(request):
    return HttpResponse('Hello, rin.')

def estrea(request):
    return HttpResponse('Hello, Estrea.')

def greet(request, name):
    return HttpResponse(f'Hello, {name.capitalize()}!')