from django.shortcuts import render
from .models import Destination, DestinationImage, Wish, Offer, CLIMATE_CHOICES, TERRAIN_CHOICES, FAMOUS_FOR_CHOICES
from .helpers import get_profile_img_url
from rest_framework import viewsets, permissions, views
from rest_framework.response import Response
from .serializers import WishSerializer


def home(request):

     context = get_profile_img_url(request.user)

     return render(request, 'home/home-page.html', context=context)


def explore(request):

     context = get_profile_img_url(request.user)
     context.update({"images" : DestinationImage.objects.all(),"offers":Offer.objects.all()})
     climate_options = [option[0] for option in CLIMATE_CHOICES]
     terrain_options = [option[0] for option in TERRAIN_CHOICES]
     famous_for_options = [option[0] for option in FAMOUS_FOR_CHOICES]
     context.update({"climate_options":climate_options,"terrain_options":terrain_options,
                     "famous_for_options":famous_for_options})

     return render(request, 'home/explore.html', context=context)


class WishViewSet(viewsets.ModelViewSet):

     authentication_classes = ()
     serializer_class = WishSerializer
     queryset = Wish.objects.all()


class DestinationNamesAPIView(views.APIView):

     authentication_classes = ()
     permission_classes = ()

     def get(self, request, format=None):

          names = [destination.name for destination in Destination.objects.all()]
          return Response(names)