from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.


def profile(request):

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
