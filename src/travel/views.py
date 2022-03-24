import requests
import stripe

from django.shortcuts import render
from django.http import Http404
from restcountries import RestCountryApiV2 as rapi

from home.models import DestinationImage, Destination, Package
from django.conf import settings as dj_settings

# Create your views here.


def travel(request, country_name):
    destination = Destination.objects.filter(name=country_name).first()
    image = DestinationImage.objects.filter(destination=destination,is_primary=True).first()
    country  = rapi.get_countries_by_name(f'{country_name}')[0]
    population = f'{country.population:,}'
    api_key = dj_settings.WEATHER_API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + country.name
    response = requests.get(complete_url).json()
    weather = response["weather"]
    response = response["main"]
    temperature = round(response["temp"] - 273.15,2)
    pressure = response["pressure"]
    humidity = response["humidity"]
    weather_description = weather[0]["description"]
    context = {"name": country.name,
               "population": population,
               "currencies" : country.currencies,
               "capital" : country.capital,
               "demonym" : country.demonym,
               "cover_img" : image,
               "temperature": temperature,
               "pressure": pressure,
               "humidity": humidity,
               "weather_description": weather_description}
    return render(request,'travel/base_travel.html',context=context)

def booking(request, package_id):
    try:
        package = Package.objects.get(id=package_id)
        stripe.api_key = dj_settings.STRIPE_API_KEY
        intent = stripe.PaymentIntent.create(
            amount=package.price,
            currency='inr',
            payment_method_types=['card'],
        )
        context = {
            "client_secret": intent.client_secret
        }
        return render(request, 'travel/booking.html', context=context)
    except Package.DoesNotExist:
        return Http404("Package Does not exist")