from django.db import models
from datetime import datetime
from .utils import create_new_sku, format_discount


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Age_range(models.Model):
    age_range = models.CharField(max_length=254)

    def __str__(self):
        return self.age_range


class Author(models.Model):
    first_name = models.CharField(max_length=254, null=True, blank=True)
    surname = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.surname}'
    
    def surname_first(self):
        return f'{self.surname}, {self.first_name}'


class Item(models.Model):

    sku = models.CharField(
        max_length=10, null=True, blank=True, 
        default=create_new_sku)
    title = models.CharField(max_length=254)
    genre = models.ManyToManyField('Genre', blank=True)
    author = models.ManyToManyField('Author', blank=True)
    description = models.TextField()
    age_range = models.ManyToManyField(
        'Age_range')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    set_sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00)
    final_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=False, editable=False)
    quantity_sold = models.DecimalField(
        max_digits=6, decimal_places=0, default=0)
    featured = models.BooleanField(default=False)
    date_added = models.DateTimeField(
        auto_now=False, auto_now_add=False, default=datetime.now)
    campaign = models.ForeignKey(
        'Campaign', on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.set_sale_price != 0.00:
            self.final_price = self.set_sale_price
        else:
            if self.discount != 0:
                formatted_discount = format_discount(self.discount)
                discount_amount = self.price * formatted_discount
                self.final_price = self.price - discount_amount
            else:
                self.final_price = self.price

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Campaign(models.Model):

    campaign_name = models.CharField(
        max_length=50, null=False, blank=False, default='Special Offer')
    active = models.BooleanField(default=True)
    fixed_price = models.DecimalField(
        max_digits=6, blank=True, null=True, decimal_places=2)

    def __str__(self):

        return self.campaign_name
