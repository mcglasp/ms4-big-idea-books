from django.shortcuts import render
from .models import Genre, Item, Author, Age_range

# Create your views here.


def all_items(request):
    """ Display the selected genre at the top of the page """
    items = Item.objects.all()

    genres = None

    if request.GET:
        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            items = items.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

    context = {
        'items': items,
        'genres': genres,
    }

    return render(request, 'items/items.html', context)
    