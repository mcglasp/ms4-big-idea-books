from django.shortcuts import render, get_object_or_404
from .models import Genre, Item, Author, Age_range

# Create your views here.


def all_items(request):
    """ Display the selected genre at the top of the page """
    items = Item.objects.all()

    genres = None
    ages = None

    if request.GET:
        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            items = items.filter(genre__name__in=genres)
            # genres = Genre.objects.filter(name__in=genres)
        
        if 'ages' in request.GET:
            ages = request.GET['ages'].split(',')
            items = items.filter(age_range__age_range__in=ages)
            # ages = Age_range.objects.filter(age_range__in=ages)

        if 'ages' in request.GET and 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            ages = request.GET['ages'].split(',')
            items = items.filter(age_range__age_range__in=ages).filter(genre__name__in=genres)
            # genres = Genre.objects.filter(name__in=genres)
            # ages = Age_range.objects.filter(age_range__in=ages)


    context = {
        'items': items,
        'genres': genres,
        'ages': ages,
    }

    return render(request, 'items/items.html', context)
    

def item_detail(request, item_id):
    """ View the selected item """
    
    item = get_object_or_404(Item, pk=item_id)
    related_lookup = item.genre.all()[0]
    related_items = Item.objects.filter(genre__name=related_lookup).exclude(id=item_id)

    context = {
        'item': item,
        'related_items': related_items,
    }

    return render(request, 'items/item_detail.html', context)
    