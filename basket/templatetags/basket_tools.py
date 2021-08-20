from django import template
from items.utils import format_discount

register = template.Library()

@register.filter(name='line_total')
def calc_line_total(price, quantity):
    return price * quantity
