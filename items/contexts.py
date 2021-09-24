from django.shortcuts import get_object_or_404
from items.models import Campaign


def special_offers(request):

    current_offers = Campaign.objects.filter(active=True)
    
    context = {
        'current_offers': current_offers,
    }

    return context
