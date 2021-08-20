from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse

from items.models import Item
from checkout.models import LineItem
# Create your views here.


def view_basket(request):

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(basket)
    return redirect(redirect_url)


def update_quantity(request, item_id):

    quantity = int(request.POST.get('quantity'))
    item = get_object_or_404(Item, pk=item_id)
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket

    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):

    basket = request.session.get('basket', {})

    basket.pop(item_id)

    request.session['basket'] = basket

    return redirect(reverse('view_basket'))

