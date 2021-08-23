from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.


def profile(request):

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        info_form = UserProfileForm(request.POST, instance=profile)
        if info_form.is_valid():
            info_form.save()

    else:
        info_form = UserProfileForm(instance=profile)
    
    orders = profile.orders.all()

    template = 'profiles/profile.html'

    context = {
        'info_form': info_form,
        'orders': orders,
    }

    return render(request, template, context)
