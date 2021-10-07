from django.shortcuts import render
from .models import DestinationImage, Wish, Offer
from .helpers import get_profile_img_url
from rest_framework import viewsets, permissions
from .serializers import WishSerializer


def home(request):

     context = get_profile_img_url(request.user)

     return render(request, 'home/home-page.html', context=context)


def explore(request):

     context = get_profile_img_url(request.user)
     context.update({"images" : DestinationImage.objects.all(),"offers":Offer.objects.all()})

     return render(request, 'home/explore.html', context=context)


class WishViewSet(viewsets.ModelViewSet):

     authentication_classes = ()
     serializer_class = WishSerializer
     queryset = Wish.objects.all()