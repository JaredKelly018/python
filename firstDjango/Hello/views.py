from django.shortcuts import render
from django.http import HttpResponse

 # Create your views here.
def index(request):
  return render(request, 'Hello/index.html')

def rin(request):
    return HttpResponse('Hello, rin.')

def estrea(request):
    return HttpResponse('Hello, Estrea.')

def greet(request, name):
    return render(request, 'Hello/greet.html'), {
        'name': name.capitalize
    }