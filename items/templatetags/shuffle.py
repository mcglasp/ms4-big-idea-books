import random
from django import template

register = template.Library()

@register.filter(name='shuffle')
def shuffle(special_offers):
    offers = list(special_offers)[:]
    random.shuffle(offers)
    return offers
