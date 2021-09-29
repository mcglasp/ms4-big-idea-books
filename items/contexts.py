from items.models import Campaign


def special_offers(request):
    """ Displays current offers across the site """
    
    current_offers = Campaign.objects.filter(active=True)
    
    context = {
        'current_offers': current_offers,
    }

    return context
