from django.shortcuts import render
from restcountries import RestCountryApiV2 as rapi
from home.models import DestinationImage, Destination
# Create your views here.


def travel(request, country_name):
    destination = Destination.objects.filter(name=country_name).first()
    image = DestinationImage.objects.filter(destination=destination,is_primary=True).first()
    country  = rapi.get_countries_by_name(f'{country_name}')[0]
    population = f'{country.population:,}'
    context = {"name": country.name,
               "population": population,
               "currencies" : country.currencies,
               "capital" : country.capital,
               "demonym" : country.demonym,
               "cover_img" : image}
    return render(request,'travel/base_travel.html',context=context)