from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def demo(request):
    return HttpResponse("<h1>Welcome</h1>")