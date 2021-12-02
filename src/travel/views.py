from django.shortcuts import render

# Create your views here.


def travel(request, country_name):
    context = {"country" : country_name}
    return render(request,'travel/base_travel.html',context=context)