from django.contrib import admin
from .models import Order, LineItem

# Register your models here.

class LineItemAdminInline(admin.TabularInline):
    model = LineItem
    readonly_fields = ('line_total',)


class OrderAdmin(admin.ModelAdmin):

    inlines = (LineItemAdminInline,)

    read_only = ('order_number', 'order_date', 'delivery_cost', 'basket_total', 'grand_total', 'original_bag', 'stripe_pid')
    
    fields = ('order_number', 'order_date', 'customer_name',
              'email_address', 'phone_number', 'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'delivery_cost',
              'basket_total', 'grand_total', 'original_basket',
              'stripe_pid')

    list_display = ('order_number', 'order_date', 'customer_name',
                    'basket_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-order_date',)

admin.site.register(Order, OrderAdmin)
