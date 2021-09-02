from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.


def profile(request):

    orders = None
    profile = get_object_or_404(UserProfile, user=request.user)
    info_form = UserProfileForm(instance=profile)

    if 'show-all' in request.GET:
        orders = profile.orders.all().order_by('-order_date')
        print(orders)

    if request.method == 'POST':
        info_form = UserProfileForm(request.POST, instance=profile)
        if info_form.is_valid():
            info_form.save()
            messages.success(request, 'Your profile has been updated.')

    if 'q' in request.GET:
        orders = profile.orders.all()
        order_query = request.GET['q']
        order_queries = Q(lineitems__item__title__icontains=order_query) | Q(order_number__icontains=order_query)
        orders = orders.filter(order_queries).distinct()

    template = 'profiles/profile.html'

    context = {
        'info_form': info_form,
        'orders': orders,
    }

    return render(request, template, context)
