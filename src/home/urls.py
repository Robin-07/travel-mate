from django.urls import path
from rest_framework import routers
from . import  views


router = routers.SimpleRouter()

router.register(r'wish', views.WishViewSet, basename='Wish')

urlpatterns = [
    path('', views.home, name="home-page"),
    path('explore/', views.explore, name="explore-page"),
    path('destinations/', views.DestinationNamesAPIView.as_view(), name="destination-names"),
    path('destinations/names/<str:name>/', views.DestinationsByNameAPIView.as_view(), name="destinations-by-name"),
    path('destinations/filters/<str:filter>/', views.DestinationsByFilterAPIView.as_view(), name="destinations-by-filter")
]

urlpatterns += router.urls