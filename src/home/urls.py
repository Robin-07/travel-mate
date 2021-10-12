from django.urls import path
from rest_framework import routers
from . import  views


router = routers.SimpleRouter()

router.register(r'wish', views.WishViewSet, basename='Wish')

urlpatterns = [
    path('', views.home, name="home-page"),
    path('explore/', views.explore, name="explore-page"),
    path('destinations/', views.DestinationNamesAPIView.as_view(), name="destination-names")
]

urlpatterns += router.urls