from django.shortcuts import render
from .models import Destination, DestinationImage


def home(request):
     return render(request, 'home/home-page.html')

def explore(request):

     images = DestinationImage.objects.all()

     return render(request, 'home/explore.html',context={"images" : images})
