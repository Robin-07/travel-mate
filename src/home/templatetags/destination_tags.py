from django import template
from django.utils.safestring import mark_safe
from home.models import Package, Wish, Offer, DestinationImage


register = template.Library()

@register.filter
def cheapest_deal(destination_id):
    return u"\u20B9" + f"{Package.objects.filter(destination=destination_id).order_by('price').values('price').first()['price']:,}"

@register.filter(is_safe=True)
def is_in_wishlist(user_id, destination_id):
    if Wish.objects.filter(user=user_id,destination=destination_id).exists():
        return mark_safe('<div class="fas fa-star fav-icon"></div>')
    return mark_safe('<div class="far fa-star fav-icon"></div>')

@register.filter
def get_offer_images(offer_id):
    return DestinationImage.objects.filter(destination=Offer.objects.get(id=offer_id).package.destination)
