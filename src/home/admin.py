from django.contrib import admin
from .models import Destination, DestinationImage, Package, Wish, Offer

# Register your models here.

admin.site.register(Destination)
admin.site.register(DestinationImage)
admin.site.register(Package)
admin.site.register(Wish)
admin.site.register(Offer)