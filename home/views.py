from django.shortcuts import render
from items.models import Item


def index(request):
    """ A view to return the index page """
    items = Item.objects.filter(active=True).order_by('-featured')

    context = {
        'items': items
    }
    return render(request, 'home/index.html', context)
