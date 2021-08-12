from django.shortcuts import render, redirect, reverse
from django.conf import settings

from .forms import OrderForm
from .models import Order, LineItem
from items.models import Item
from profiles.models import UserProfile
from basket.contexts import basket_contents

import stripe
import json


# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == "POST":

        basket = request.session.get('basket', {})

        form_values = {
            'customer_name': request.POST['customer_name'],
            'email_address': request.POST['email_address'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }

        order_form = OrderForm(form_values)

        if order_form.is_valid():
            order = order_form.save()

            order.save()

            for item_id, item_data in basket.items():

                item = Item.objects.get(id=item_id)
                line_item = LineItem(
                    related_order=order,
                    item=item,
                    quantity=item_data,
                )

                line_item.save()

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('items'))

        else:
            print('There was an error with your form.')

    else:
        basket = request.session.get('basket', {})

        if not basket:
            print("there's nothing there")
            return redirect(reverse('items'))

        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'customer_name': profile.user,
                'email_address': profile.default_email_address,
                'phone_number': profile.default_phone_number,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
            })

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total*100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        print(intent)       
        print(total)

        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'total': total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

    # 4000058260000005