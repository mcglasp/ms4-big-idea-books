from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.db.models import F, Q, Func
from django.db.models.functions import Lower
from django.contrib import messages

from basket.views import remove_from_basket

from .models import Genre, Item, Author, Age_range
from .forms import ItemForm, AuthorDataForm
from .templatetags.price_tools import calc_discounted_price
from softdelete.models import SoftDeleteRecord

import json



# Create your views here.


def all_items(request):
    try:
        items = Item.objects.all().order_by('-featured', 'quantity_sold')
    except:
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
                sort_by = 'final_price'

            if sort_by == 'price_high_low':
                sort_by = '-final_price'

            if sort_by == 'title_az':
                items = items.annotate(lower_title=Lower('title'))
                sort_by = 'lower_title'

            if sort_by == 'most_discounted':
                items = items.annotate(discount_amount=F('price') - F('final_price'))
                sort_by = '-discount_amount'

            if sort_by == 'quantity_sold':
                sort_by = '-quantity_sold'

            items = items.order_by(sort_by)

        if 'genres' in request.GET and 'ages' not in request.GET:
            genres = request.GET['genres'].split(',')
            items = items.filter(genre__name__in=genres)
            narrow_age = None if items.count() == 0 else True
        
        if 'ages' in request.GET and 'genres' not in request.GET:
            ages = request.GET['ages'].split(',')
            items = items.filter(age_range__age_range__in=ages)
            narrow_genre = None if items.count() == 0 else True

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
        'search_term': user_query,
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


def add_item(request):
    authors_select = Author.objects.all()

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        title = request.POST.get("title")
        description = request.POST.get("description")
        
        if form.is_valid():
            check_item = Item.objects.filter(title=title, description=description)
            if check_item.exists() is True:
                messages.error(request, "There's a book in the shop with this title and description. Please check your existing items and make this listing unique.")
            else:
                form.save()
                saved_item = Item.objects.get(title=title, description=description)
                item_id = saved_item.id
                instance = get_object_or_404(Item, pk=item_id)
                author_array = request.POST.get("authors")
                authors = author_array.split(';')
                for author in authors:
                    if len(author) > 0:
                        first = author.split(" ")[0]
                        last = author.split(" ")[1]
                        this_author = Author.objects.get_or_create(first_name=first, surname=last)
                        (name, disregard) = this_author
                        author_to_attach = name
                        instance.author.add(author_to_attach)
                        messages.success(request, f"{title} has been added to the shop")
        else:
            messages.error(request, "There's something wrong with your form, please check for errors.")
            return redirect(reverse('add_item'))
    else:
        form = ItemForm()

    context = {
        'form': form,
        'authors_select': authors_select,
    }

    return render(request, 'items/add_item.html', context)


def update_item(request, item_id):

    authors_select = Author.objects.all()

    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            author_array = request.POST.get("authors")
            authors = author_array.split(';')
            for author in authors:
                if len(author) > 0:
                    first = author.split(" ")[0]
                    last = author.split(" ")[1]
                    this_author = Author.objects.get_or_create(first_name=first, surname=last)
                    (name, disregard) = this_author
                    author_to_attach = name
                    item.author.add(author_to_attach)
        
            messages.success(request, 'This item has been successfully updated.')
            return redirect(reverse('item_detail', args=[item.id]))

        else:
            messages.error(request, 'Failed to update product. Please check form fields.')
    else:
        form = ItemForm(instance=item)

    template = 'items/update_item.html'
    context = {
        'form': form,
        'item': item,
        'authors_select': authors_select,
    }
    
    return render(request, template, context)


def delete_item(request, item_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can do that.')
        return redirect(reverse('home'))
   
    item = get_object_or_404(Item, pk=item_id)
    print(item_id)
    item.delete()
    messages.success(request, 'Product successfully deleted!')

    return redirect(reverse('items'))


def add_author(request):

    if request.method == 'POST':
        author_form = AuthorDataForm(request.POST, request.FILES)
        if author_form.is_valid():
            author_form.save()
            messages.success(request, 'Author added.')

    else:
        author_form = AuthorDataForm(request.POST, request.FILES)

    context = {
        'author_form': author_form,
    }

    return render(request, 'items/add_author.html', context)
