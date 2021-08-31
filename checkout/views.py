from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages

from .forms import OrderForm
from profiles.forms import UserProfileForm
from .models import Order, LineItem
from items.models import Item
from profiles.models import UserProfile
from basket.contexts import basket_contents

import stripe
import json


# Create your views here.


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, we cannot process your payment right now.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    payment_process_info = ""

    if request.method == "POST":

        basket = request.session.get('basket', {})

        form_values = {
            'customer_name': request.POST['customer_name'],
            'phone_number': request.POST['phone_number'],
            'email_address': request.POST['email_address'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
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
                item.quantity_sold = line_item.quantity + item.quantity_sold
                item.save(update_fields=['quantity_sold'])
                line_item.save()

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('order_confirmation', args=[order.order_number]))

        else:
            payment_process_info = "Something isn't quite right. Please check your form and try again"

    else:
        basket = request.session.get('basket', {})

        if not basket:
            messages.error(request, 'Sorry, there is nothing in your basket.')
            return redirect(reverse('items'))

        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'customer_name': profile.user,
                'phone_number': profile.default_phone_number,
                'email_address': profile.default_email_address,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'town_or_city': profile.default_town_or_city,
                'postcode': profile.default_postcode,
            })
        
        else:
            order_form = OrderForm()

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total*100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'total': total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'payment_process_info': payment_process_info,
    }
    return render(request, template, context)


def order_confirmation(request, order_number):
   
    order = get_object_or_404(Order, order_number=order_number)
    
    save_info = request.session.get('save_info')

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            default_data = {
                'default_phone_number': order.phone_number,
                'default_email_address': order.email_address,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_postcode': order.postcode,
            }

            user_profile_form = UserProfileForm(default_data, instance=profile)

            if user_profile_form.is_valid():
                user_profile_form.save()

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/order_confirmation.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

    # 4000058260000005