from django.shortcuts import render
from .models import Destination, DestinationImage
from .helpers import get_profile_img_url

def home(request):

     context = get_profile_img_url(request.user)

     return render(request, 'home/home-page.html', context=context)

def explore(request):

     context = get_profile_img_url(request.user)

     context.update({"images" : DestinationImage.objects.all()})

     return render(request, 'home/explore.html', context=context)
