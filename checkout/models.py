from django.db import models
from django.db.models import Sum
from django.conf import settings

from items.models import Item
from profiles.models import UserProfile
from .utils import create_order_number

# Create your models here.

class Order(models.Model):

    order_number = models.CharField(
        max_length=15, null=True, blank=True, 
        default=create_order_number) 
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    customer_name = models.CharField(max_length=60, null=False, blank=False)
    email_address = models.EmailField(max_length=254, null=False, blank=False, default='not_given')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=3, decimal_places=2, null=False, default=settings.STANDARD_DELIVERY_COST, editable=False)
    basket_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    # def calculate_total(self):

    #     self.basket_total = self.lineitems.aggregate(Sum('line_total'))['line_total__sum']
    #     self.grand_total = float(self.basket_total) + settings.STANDARD_DELIVERY_COST
    #     self.save()

    def __str__(self):

        return self.order_number


class LineItem(models.Model):

    related_order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    item = models.ForeignKey(Item, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):

        self.line_total = self.item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.item.sku} on order {self.related_order.order_number}'