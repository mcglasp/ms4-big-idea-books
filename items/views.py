from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.db.models import F, Q, ExpressionWrapper, DecimalField
from django.db.models.functions import Lower
from django.contrib import messages

from .models import Genre, Item, Author, Age_range
from .forms import ItemForm, AuthorDataForm



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
        if 'sort' in request.GET:
            sort_by = request.GET['sort']
            if sort_by == 'price_low_high':
                sort_by = 'price'

            if sort_by == 'price_high_low':
                sort_by = '-price'

            if sort_by == 'title_az':
                items = items.annotate(lower_title=Lower('title'))
                sort_by = 'lower_title'

            if sort_by == 'most_discounted':
                items = items.annotate(price_difference=F('price') * F('discount'))
                sort_by = '-price_difference'
            
            if sort_by == 'quantity_sold':
                sort_by = 'quantity_sold'

            items = items.order_by(sort_by)

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
            
            user_queries = Q(title__icontains=user_query) | Q(description__icontains=user_query) | Q(genre__name__icontains=user_query) | Q(author__first_name__icontains=user_query) | Q(author__surname__icontains=user_query)
            items = items.filter(user_queries).distinct()

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
    for age in item.age_range.all():
        if age == 'preschool':
            print('hi', age)
    related_lookup = item.genre.all()[0]
    related_items = Item.objects.filter(genre__name=related_lookup).exclude(id=item_id)

    context = {
        'item': item,
        'related_items': related_items,
    }

    return render(request, 'items/item_detail.html', context)


def add_item(request):

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            if form.data['discount'] is not '0':
                discount_amount = form.data['discount']
                float(discount_amount) / 100
                form.save()
            else:
                form.save()
    
    else:
        form = ItemForm()

    context = {
        'form': form,
    }

    return render(request, 'items/add_item.html', context)


def update_item(request, item_id):

    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Failed to update product. Please check form fields.')

            return redirect(reverse('item_detail', args=[item.id]))
        else:
            messages.error(request, 'Failed to update product. Please check form fields.')
    else:
        form = ItemForm(instance=item)

    form = ItemForm(instance=item)

    template = 'items/update_item.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


def delete_item(request, item_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can do that.')
        return redirect(reverse('home'))
        
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    messages.success(request, 'Product successfully deleted!')

    return redirect(reverse('items'))


def add_author(request):

    if request.method == 'POST':
        author_form = AuthorDataForm(request.POST, request.FILES)
        if author_form.is_valid():
            author_form.save()

    else:
        author_form = AuthorDataForm(request.POST, request.FILES)

    context = {
        'author_form': author_form,
    }

    return render(request, 'items/add_author.html', context)
