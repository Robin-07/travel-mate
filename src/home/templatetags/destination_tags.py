from django import template
from django.utils.safestring import mark_safe
from home.models import Package, Wish


register = template.Library()

@register.filter
def cheapest_deal(destination):
    return u"\u20B9" + f"{Package.objects.filter(destination=destination).order_by('price').values('price').first()['price']:,}"

@register.filter(is_safe=True)
def is_in_wishlist(user, destination):
    if Wish.objects.filter(user=user,destination=destination).exists():
        return mark_safe('<div class="fas fa-star fav-icon"></div>')
    return mark_safe('<div class="far fa-star far fav-icon"></div>')
