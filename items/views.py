from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Genre, Item, Author, Age_range
from django.db.models.functions import Lower


# Create your views here.


def all_items(request):
    items = Item.objects.all()

    genres = None
    ages = None
    narrow_age = None
    narrow_genre = None
    user_query = None
    sort_by = None

    if request.GET:
        if 'genres' in request.GET and 'ages' not in request.GET:
            genres = request.GET['genres'].split(',')
            items = items.filter(genre__name__in=genres)
            narrow_age = True
        
        if 'ages' in request.GET and 'genres' not in request.GET:
            ages = request.GET['ages'].split(',')
            items = items.filter(age_range__age_range__in=ages)
            narrow_genre = True

        if 'genres_narrow' in request.GET:
            genres = request.GET['genres_narrow'].split(',')
            ages = request.GET['ages'].split(',')
            items = items.filter(age_range__age_range__in=ages).filter(
                                 genre__name__in=genres)

        if 'ages_narrow' in request.GET:
            ages = request.GET['ages_narrow'].split(',')
            genres = request.GET['genres'].split(',')
            items = items.filter(genre__name__in=genres).filter(
                                age_range__age_range__in=ages)

        if 'q' in request.GET:
            user_query = request.GET['q']
            
            user_queries = Q(title__icontains=user_query) | Q(description__icontains=user_query)| Q(genre__name__icontains=user_query) | Q(author__first_name__icontains=user_query)
            items = items.filter(user_queries).distinct()

        if 'sort' in request.GET:
            sort_by = request.GET['sort']
            if sort_by == 'price_low_high':
                sort_by = '-price'
                # items = items.order_by(sort_by)

            if sort_by == 'price_high_low':
                sort_by = 'price'
                # items = items.order_by(sort_by)

            if sort_by == 'title_az':
                items = items.annotate(lower_title=Lower('title'))
                sort_by = 'lower_title'
            
            items = items.order_by(sort_by)

    

    context = {
        'items': items,
        'genres': genres,
        'ages': ages,
        'narrow_age': narrow_age,
        'narrow_genre': narrow_genre,
        'sort_by': sort_by,
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
    