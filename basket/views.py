from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from items.models import Item
from checkout.models import LineItem


def view_basket(request):
    """ Returns the full-page basket view """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Adds an item to the basket without refreshing the page """

    item = Item.objects.get(pk=item_id)
    if item.active:
        redirect_url = request.POST.get('redirect_url')
        quantity = int(request.POST.get('quantity'))
        basket = request.session.get('basket', {})

        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity
    
        messages.success(request, f'{item.title} has been added to your basket.')
        request.session['basket'] = basket
        return redirect(redirect_url)

    else: 
        messages.error(request, f'Sorry, {item.title} is not currently available.')
        return redirect('items')



def update_quantity(request, item_id):
    """Update quantity of item in basket from full-page basket view"""

    quantity = int(request.POST.get('quantity'))
    item = get_object_or_404(Item, pk=item_id)
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, 'Your basket has been updated.')

    else:
        basket.pop(item_id)
        messages.success(request, f'{item.title} has been removed from your basket.')

    request.session['basket'] = basket

    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove item from basket from full-page basket view"""

    basket = request.session.get('basket', {})
    item = get_object_or_404(Item, pk=item_id)
    basket.pop(item_id)
    request.session['basket'] = basket
    messages.success(request, f'{item.title} has been removed from your basket.')

    return redirect(reverse('view_basket'))

