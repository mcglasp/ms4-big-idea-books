from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.


def profile(request):

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        info_form = UserProfileForm(request.POST, instance=profile)
        if info_form.is_valid():
            info_form.save()

    info_form = UserProfileForm(instance=profile)
    
    orders = profile.orders.all()


    if 'q' in request.GET:
        order_query = request.GET['q']
        order_queries = Q(lineitems__item__title__icontains=order_query)
        orders = orders.filter(order_queries).distinct()

    template = 'profiles/profile.html'

    context = {
        'info_form': info_form,
        'orders': orders,
    }

    return render(request, template, context)
