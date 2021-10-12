from django import template
from django.utils.safestring import mark_safe
from home.models import Package, Wish, Offer, DestinationImage


register = template.Library()

@register.filter
def cheapest_deal(destination_id):
    return u"\u20B9" + f"{Package.objects.filter(destination=destination_id).order_by('price').values('price').first()['price']:,}"

@register.filter(is_safe=True)
def is_in_wishlist(user_id, destination_id):
    wish = Wish.objects.filter(user=user_id,destination=destination_id)
    if wish.exists():
        return mark_safe(f'<div data-toggle="tooltip" title="Bookmarked" class="fas fa-bookmark fav-icon" onclick="toggleWish(event,{wish.first().id},0)"></div>')
    return mark_safe(f'<div data-toggle="tooltip" title="Bookmark" class="far fa-bookmark fav-icon" onclick="toggleWish(event,0,{destination_id})"></div>')

@register.filter
def get_offer_images(offer_id):
    return DestinationImage.objects.filter(destination=Offer.objects.get(id=offer_id).package.destination)
