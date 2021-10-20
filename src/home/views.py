from django.shortcuts import render, HttpResponse
from .models import Destination, DestinationImage, Package, Wish, Offer, CLIMATE_CHOICES, TERRAIN_CHOICES, FAMOUS_FOR_CHOICES
from .helpers import get_profile_img_url
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from .serializers import WishSerializer
from django.db.models import Q
from .forms import ProfileForm
from authentication.models import User, UserProfile


def Index(request):

     if request.user.is_authenticated:
          return Explore(request)

     context = get_profile_img_url(request.user)

     return render(request, 'home/home-page.html', context=context)


def Explore(request):

     context = get_profile_img_url(request.user)
     context.update({"images" : DestinationImage.objects.all(),"offers":Offer.objects.all()})
     climate_options = [option[0] for option in CLIMATE_CHOICES]
     terrain_options = [option[0] for option in TERRAIN_CHOICES]
     famous_for_options = [option[0] for option in FAMOUS_FOR_CHOICES]
     context.update({"climate_options":climate_options,"terrain_options":terrain_options,
                     "famous_for_options":famous_for_options})

     return render(request, 'home/explore.html', context=context)

def Profile(request):

     if request.method == "GET":
          user = User.objects.filter(id=request.user.id).first()
          profile = UserProfile.objects.filter(user=user).first()
          context = {}

     elif request.method == "POST":
          user = User.objects.filter(id=request.user.id).first()
          profile = UserProfile.objects.filter(user=user).first()
          form = ProfileForm(request.POST, request.FILES)

          if form.is_valid():

               first_name = form.cleaned_data.get('first_name')
               last_name = form.cleaned_data.get('last_name')
               photo = form.cleaned_data.get('photo')
               phone = form.cleaned_data.get('phone')
               dob = form.cleaned_data.get('dob')

               if(first_name):
                    user.first_name = first_name
               if (last_name):
                    user.last_name = last_name
               if (photo):
                    profile.photo = photo
               if (phone):
                    profile.phone = phone
               if (dob):
                    profile.dob = dob

               user.save()
               profile.save()

               context = {"msg" : "Profile Updated Successfully", "msgColor": "green"}

          else:
               context = {"msg" : "Failed to Update Profile. Please try again", "msgColor": "red"}

     defaults = {"first_name": user.first_name, "last_name": user.last_name,
                 "phone": profile.phone, "dob": profile.dob, "photo": profile.photo}
     form = ProfileForm(initial=defaults)
     context.update({"form": form})
     context.update(get_profile_img_url(user))
     return render(request, 'home/profile.html', context=context)


class WishViewSet(viewsets.ModelViewSet):

     authentication_classes = ()
     serializer_class = WishSerializer
     queryset = Wish.objects.all()


class DestinationNamesAPIView(views.APIView):

     authentication_classes = ()

     def get(self, request):
          names = [destination.name for destination in Destination.objects.all()]
          return Response(data = names, status=status.HTTP_200_OK)


# APIViews for Destination Search

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