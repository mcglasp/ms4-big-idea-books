from django.conf import settings
from django.shortcuts import get_object_or_404
from items.models import Item


def basket_contents(request):

    basket = request.session.get('basket', {})
    basket_items = []

    for item_id, value in basket.items():
        item = get_object_or_404(Item, pk=item_id)
        basket_items.append({
            'item_id': int(item_id),
            'item': item,
            'price': item.price,
            'quantity': value,
        })

    context = {
        'basket_items': basket_items,
    }

    return context
