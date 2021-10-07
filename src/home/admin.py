from django.contrib import admin
from .models import Destination, DestinationImage, Package, Wish

# Register your models here.

admin.site.register(Destination)
admin.site.register(DestinationImage)
admin.site.register(Package)
admin.site.register(Wish)