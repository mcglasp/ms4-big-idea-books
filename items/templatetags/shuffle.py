import random
from django import template

# This function shuffles the order of the active campaigns queryset, 
# the first of which is displayed on the Index page. 
# Shuffling the set ensures that the displayed campaign changes.

register = template.Library()

# CREDIT christophe31 of Stackoverflow

@register.filter(name='shuffle')
def shuffle(special_offers):
    offers = list(special_offers)[:]
    random.shuffle(offers)
    return offers
