from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer_name', 'email_address', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode',
                )

    # def __init__(self, *args, **kwargs):
    #     """
    #     Add placeholders and classes, remove auto-generated
    #     labels and set autofocus on first field
    #     """
    #     super().__init__(*args, **kwargs)
    #     placeholders = {
    #         'customer_name': 'Full Name',
    #         'email_address': 'Email Address',
    #         'phone_number': 'Phone Number',
    #         'postcode': 'Postal Code',
    #         'town_or_city': 'Town or City',
    #         'street_address1': 'Street Address 1',
    #         'street_address2': 'Street Address 2',
    #     }