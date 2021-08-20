from django import template
from items.utils import format_discount
from items.models import Item

register = template.Library()

@register.filter(name='calc_discount')
def calc_discounted_price(price, discount):
    formatted_discount = format_discount(discount)
    item_discount = price * formatted_discount
    discounted_price = price - item_discount
    return round(discounted_price, 2)
