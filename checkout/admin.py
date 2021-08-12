from django.contrib import admin
from .models import Order, LineItem

# Register your models here.

class LineItemAdminInline(admin.TabularInline):
    model = LineItem
    readonly_fields = ('line_total',)


class OrderAdmin(admin.ModelAdmin):

    inlines = (LineItemAdminInline,)

    read_only = ('order_number', 'order_date', 'delivery_cost', 'basket_total', 'grand_total',
                )

admin.site.register(Order, OrderAdmin)
