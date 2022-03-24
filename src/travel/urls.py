from django.urls import path
from . import views

urlpatterns = [
    path('<str:country_name>', views.travel, name='travel'),
    path('booking/<int:package_id>', views.booking, name='booking')
]