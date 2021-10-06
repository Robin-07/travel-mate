from django import template
from home.models import Deal


register = template.Library()

@register.filter
def cheapest_deal(destination):
    print(destination)
    return u"\u20B9" + f"{Deal.objects.filter(destination=destination).order_by('price').values('price').first()['price']:,}"
