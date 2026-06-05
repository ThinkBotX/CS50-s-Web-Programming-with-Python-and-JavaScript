from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def anas(request):
    return HttpResponse("Hello, Anas!")

def ali(request):
    return HttpResponse("Hello, Ali!")