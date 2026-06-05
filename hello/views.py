from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def anas(request):
    return render(request, "hello/anas.html")

def ali(request):
    return render(request, "hello/ali.html")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })