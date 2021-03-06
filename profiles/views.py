from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from items.models import Item


@login_required
def profile(request):
    """
    Displays a logged-in user's default details and order history
    """
    # check for any previous orders
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = None
    previous_orders = profile.orders.all()

    if previous_orders:
        previous_orders = True
    else:
        previous_orders = False

    info_form = UserProfileForm(instance=profile)

    if 'show-all' in request.GET:
        orders = profile.orders.all().order_by('-order_date')

    if request.method == 'POST':
        info_form = UserProfileForm(request.POST, instance=profile)
        if info_form.is_valid():
            info_form.save()
            messages.success(request, 'Your profile has been updated.')

    if 'q' in request.GET:
        order_query = request.GET['q']
        order_queries = (
                Q(lineitems__item__title__icontains=order_query) |
                Q(order_number__icontains=order_query) |
                Q(lineitems__item__author__first_name__icontains=order_query) |
                Q(lineitems__item__author__surname__icontains=order_query) |
                Q(lineitems__item__genre__name__icontains=order_query)
                )
        orders = profile.orders.filter(order_queries).distinct()

    template = 'profiles/profile.html'

    context = {
        'info_form': info_form,
        'orders': orders,
        'previous_orders': previous_orders,
    }

    return render(request, template, context)
