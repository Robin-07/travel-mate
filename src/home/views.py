from django.shortcuts import render
from .models import Destination, DestinationImage, Package, Wish, Offer, CLIMATE_CHOICES, TERRAIN_CHOICES, FAMOUS_FOR_CHOICES
from .helpers import get_profile_img_url
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from .serializers import WishSerializer
from django.db.models import Q


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

     def get(self, request):

          names = [destination.name for destination in Destination.objects.all()]
          return Response(data = names, status=status.HTTP_200_OK)


class DestinationsByNameAPIView(views.APIView):

     authentication_classes = ()

     def get(self, request, name):

          destination = Destination.objects.filter(name=name).first()
          if not destination:
               return Response(data={"error":"No Results Found"},status=status.HTTP_404_NOT_FOUND)
          destination_images = DestinationImage.objects.filter(destination=destination)
          image_url = ""
          for image in destination_images:
               if image.is_primary:
                    image_url = image.image_url
          cheapest_deal = Package.objects.filter(destination=destination.id).order_by('price').values('price').first()['price']
          return Response(data=[{"name":destination.name,"image_url":image_url,"cheapest_deal":cheapest_deal}],status=status.HTTP_200_OK)


class DestinationsByFilterAPIView(views.APIView):

     authentication_classes = ()

     def get(self, request, filter):

          destinations = Destination.objects.filter(Q(famous_for=filter) | Q(climate_type=filter) | Q(terrain_type=filter))
          if not destinations:
               return Response(data={"error": "No Results Found"}, status=status.HTTP_404_NOT_FOUND)
          resp = []
          for destination in destinations:
               destination_images = DestinationImage.objects.filter(destination=destination)
               image_url = ""
               for image in destination_images:
                    if image.is_primary:
                         image_url = image.image_url
               cheapest_deal = Package.objects.filter(destination=destination.id).order_by('price').values('price').first()['price']
               resp.append({"name":destination.name,"image_url":image_url,"cheapest_deal":cheapest_deal})
          return Response(data = resp, status = status.HTTP_200_OK)