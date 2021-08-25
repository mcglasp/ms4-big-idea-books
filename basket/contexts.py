from django.conf import settings
from django.shortcuts import get_object_or_404
from items.models import Item


def basket_contents(request):

    basket = request.session.get('basket', {})
    basket_items = []
    total_items = 0
    total = 0
    price = 0
    delivery_cost = settings.STANDARD_DELIVERY_COST

    def update_item_price(price, discount, set_sale_price):
        set_sale_price = float(item.set_sale_price)
        discount_percentage = float(item.discount) / 100
        if set_sale_price > 0:
            price = set_sale_price
        else:
            if discount_percentage > 0:
                float_price = float(price)
                money_off = float_price * discount_percentage
                price = round(float_price - money_off, 2)
            else:
                price = item.price
        return price
        
    if basket:

        for item_id, value in basket.items():
            if isinstance(value, int):  
                item = get_object_or_404(Item, pk=item_id)
                price = update_item_price(item.price, item.discount, 
                        item.set_sale_price)
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
