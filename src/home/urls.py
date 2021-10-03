from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('explore/', views.explore, name="explore-page"),
]