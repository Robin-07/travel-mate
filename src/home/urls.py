from django.urls import path
from rest_framework import routers
from . import  views


router = routers.SimpleRouter()

router.register(r'wish', views.WishViewSet, basename='Wish')

urlpatterns = [
    path('', views.Index, name="home-page"),
    path('explore/', views.Explore, name="explore-page"),
    path('profile/', views.Profile, name="edit-profile"),
    path('destinations/', views.DestinationNamesAPIView.as_view(), name="destination-names"),
    path('destinations/names/<str:name>/', views.DestinationsByNameAPIView.as_view(), name="destinations-by-name"),
    path('destinations/filters/<str:filter>/', views.DestinationsByFilterAPIView.as_view(), name="destinations-by-filter")
]

urlpatterns += router.urls