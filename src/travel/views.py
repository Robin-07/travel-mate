import requests
import stripe

from django.shortcuts import render, redirect
from restcountries import RestCountryApiV2 as rapi

from home.models import DestinationImage, Destination, Package
from .models import Invoice
from django.conf import settings as dj_settings

BASE_TRAVEL_URL = "http://127.0.0.1:8000/travel/"

# Create your views here.


def travel(request, country_name):
    if request.method == "GET":
        destination = Destination.objects.get(name=country_name)
        image = DestinationImage.objects.get(destination=destination,is_primary=True)
        country = rapi.get_countries_by_name(f'{country_name}')[0]
        population = f'{country.population:,}'

        url = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" \
              + dj_settings.WEATHER_API_KEY + "&q=" + country.name
        response = requests.get(url).json()
        weather_description = response["weather"][0]["description"]
        response = response["main"]
        temperature = round(response["temp"] - 273.15, 2)

        msg = request.GET.get("msg")
        success_msg = False
        if msg is None:
            checkout_msg = ""
        elif msg == "checkout-success":
            checkout_msg = "Congratulations! Your Checkout was successful"
            success_msg = True
        else:
            checkout_msg = "Unfortunately, Your Checkout was not successful"

        context = {
            "name": country.name,
            "population": population,
            "currencies": country.currencies,
            "capital": country.capital,
            "demonym": country.demonym,
            "cover_img": image,
            "temperature": temperature,
            "pressure": response["pressure"],
            "humidity": response["humidity"],
            "weather_description": weather_description,
            "checkout_msg": checkout_msg,
            "success_msg": success_msg
        }

        return render(request, 'travel/base_travel.html', context=context)


def create_checkout_session(request, package_id):
    if request.method == "GET":
        try:
            package = Package.objects.select_related('destination').get(id=package_id)
            Invoice.objects.create(package=package, user=request.user)
            stripe.api_key = dj_settings.STRIPE_API_KEY
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'inr',
                            'unit_amount': package.price * 100,
                            'product_data': {
                                'name': package.destination.name
                            }
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=BASE_TRAVEL_URL + f'{package.destination.country}?msg=checkout-success',
                cancel_url=BASE_TRAVEL_URL + f'{package.destination.country}?msg=checkout-cancel',
            )
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            print(e)
            return redirect('http://127.0.0.1:8000/explore/')
