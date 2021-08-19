from django.conf import settings
from django.shortcuts import get_object_or_404
from items.models import Item


def basket_contents(request):

    basket = request.session.get('basket', {})
    basket_items = []
    total_items = 0
    total = 0

    if basket:

        for item_id, value in basket.items():
            if isinstance(value, int):  
                item = get_object_or_404(Item, pk=item_id)
                total += value * item.price
                total_items += value
                basket_items.append({
                    'item_id': int(item_id),
                    'item': item,
                    'price': item.price,
                    'quantity': value,
                })

        delivery_cost = settings.STANDARD_DELIVERY_COST

        grand_total = delivery_cost + float(total)
    
    else:
        grand_total = 0

    context = {
        'basket_items': basket_items,
        'total_items': total_items,
        'grand_total': grand_total,

    }

    return context
