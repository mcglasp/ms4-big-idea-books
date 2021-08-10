from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
    
    # def __init__(self, *args, **kwargs):

    #     super().__init__(*args, **kwargs)
    #     placeholders = {
    #         'default_phone_number': 'Phone Number',
    #         'default_postcode': 'Postal Code',
    #         'default_town_or_city': 'Town or City',
    #         'default_street_address1': 'Street Address 1',
    #         'default_street_address2': 'Street Address 2',
    #     }