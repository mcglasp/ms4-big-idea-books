from django.conf import settings
from django.shortcuts import get_object_or_404
from items.models import Item, Campaign
from django.contrib import messages


def basket_contents(request):

    basket = request.session.get('basket', {})
    dict_to_compare = basket

    d_keys = dict_to_compare.keys()

# Check for deleted database items in existing basket
    for key in list(d_keys):
        is_in_db = Item.objects.filter(id=key).exists()
        if is_in_db:
            continue
        else:
            dict_to_compare.pop(key)
            messages.error(request, "An item in your basket has been deleted as it is not currently available.")
  
    dict_to_compare = basket

    basket_items = []
    total_items = 0
    total = 0
    price = 0
    delivery_cost = settings.STANDARD_DELIVERY_COST
    basket = request.session.get('basket', {})
     
    if basket:
        for item_id, value in basket.items():
            if isinstance(value, int):
                item = get_object_or_404(Item, pk=item_id)
                price = item.final_price
                val_float = float(value)
                total += val_float * float(price)
                total_items += value
                basket_items.append({
                    'item_id': int(item_id),
                    'item': item,
                    'price': price,
                    'quantity': value,
                })
                
        total = round(total, 2)
        grand_total = round(delivery_cost + float(total), 2)
    
    else:
        grand_total = 0

    context = {
        'basket_items': basket_items,
        'total_items': total_items,
        'price': price,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
        'basket_total': total,
    }

    return context


