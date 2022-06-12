from django.urls import path
from . import views

urlpatterns = [
    path('<str:country_name>', views.travel, name='travel'),
    path('create-checkout-session/<int:package_id>', views.create_checkout_session, name='create-checkout-session')
]