from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import F, Q
from django.db.models.functions import Lower
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db import IntegrityError
from .models import Item, Author, Campaign
from .forms import ItemForm, AuthorDataForm, CampaignForm


def all_items(request):
    """ 
    Displays all items available on the store
    and manages filtering and sorting
    """

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

            if sort_by == 'newly_listed':
                sort_by = '-date_added'

            if sort_by == 'featured':
                sort_by = '-featured'

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
            user_queries = Q(title__icontains=user_query) | Q(description__icontains=user_query) | Q(genre__name__icontains=user_query) | Q(author__first_name__icontains=user_query) | Q(author__surname__icontains=user_query) | Q(age_range__age_range__icontains=user_query)
            items = items.filter(user_queries).distinct() 
    
    featured = items.filter(featured=True).exists()
    items = items.filter(active=True)
    context = {
        'featured': featured,
        'items': items,
        'genres': genres,
        'ages': ages,
        'narrow_age': narrow_age,
        'narrow_genre': narrow_genre,
        'search_term': user_query,
        'sort_by': sort_by,
    }

    return render(request, 'items/items.html', context)
    

def latest_items(request):
    """
    Displays the 10 most recently added items
    """

    items = Item.objects.filter(active=True).order_by('-date_added')[:10]
    context = {
        "items": items
    }

    return render(request, 'items/items.html', context)


def go_to_offer(request, offer_id):
    """
    View the advertised sales campaign
    """

    offer = get_object_or_404(Campaign, pk=offer_id)
    items = Item.objects.filter(campaign__pk=offer_id).filter(active=True)
 
    context = {
        'offer': offer,
        'items': items,
    }

    return render(request, 'items/items.html', context)


def item_detail(request, item_id):
    """
    Detailed view of a single product.
    Also returns related items
    """

    item = get_object_or_404(Item, pk=item_id)

    if item.active:
        related_genres = item.genre.all()
        if related_genres.count() > 1:
            rel_1 = related_genres[0].item_set.count()
            rel_2 = related_genres[1].item_set.count()
            if rel_1 > rel_2:
                related_lookup = related_genres[0]
            else:
                related_lookup = related_genres[1]
        else:
            related_lookup = related_genres[0]

        related_items = Item.objects.filter(
            genre__name=related_lookup).exclude(id=item_id).filter(
            active=True).exclude(image='')
        
        if related_items.count() == 0:
            related_items = Item.objects.exclude(id=item_id).filter(
                active=True).exclude(image='').order_by('-date_added')
    
    else:
        messages.error(request, 'Sorry, that item is not currently available.')
        return redirect('items')

    context = {
        'item': item,
        'related_items': related_items,
    }

    return render(request, 'items/item_detail.html', context)


@login_required
@staff_member_required
def add_item(request):
    """
    Add an item to the store
    """

    authors_select = Author.objects.all()

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        title = request.POST.get("title")
        description = request.POST.get("description")
        if form.is_valid():
            check_item = Item.objects.filter(
                title=title, description=description)
            if check_item.exists() is True:
                messages.error(
                    request, 'There is a book in the shop with this title and'
                    'description. Please check your existing items and make' 
                    'this listing unique.')
            else:
                form.save()
                saved_item = Item.objects.get(
                    title=title, description=description)
                item_id = saved_item.id
                instance = get_object_or_404(Item, pk=item_id)
                # Add author to database if not already added, 
                # associate it with added item
                author_array = request.POST.get("authors")
                authors = author_array.split(';')
                for author in authors:
                    if len(author) > 0:
                        first = author.split(" ")[0]
                        last = author.split(" ")[1]
                        this_author = Author.objects.get_or_create(
                            first_name=first, surname=last)
                        (name, disregard) = this_author
                        author_to_attach = name
                        instance.author.add(author_to_attach)
                
                messages.success(request, f"{title} has been added to the shop")
                return redirect('add_item')
        else:
            
            form = ItemForm(request.POST, request.FILES)
            messages.error(request, 'There is something wrong with your form,'
                                    'please check for errors.')
            
    else:
        form = ItemForm()

    context = {
        'form': form,
        'authors_select': authors_select,
    }


    return render(request, 'items/add_item.html', context)

@login_required
@staff_member_required
def update_item(request, item_id):
    """ 
    A view to update existing product information.
    """
    
    authors_select = Author.objects.all()

    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            # Add author to database if not already added, 
            # associate it with added item
            author_array = request.POST.get("authors")
            authors = author_array.split(';')
            for author in authors:
                if len(author) > 0:
                    first = author.split(" ")[0]
                    last = author.split(" ")[1]
                    this_author = Author.objects.get_or_create(
                        first_name=first, surname=last)
                    (name, disregard) = this_author
                    author_to_attach = name
                    item.author.add(author_to_attach)
        
            messages.success(request, 'This item has been successfully updated.')
            return redirect(reverse('item_detail', args=[item.id]))

        else:
            messages.error(
                request, 'Failed to update product. Please check form fields.')
    else:
        form = ItemForm(instance=item)

    template = 'items/update_item.html'
    context = {
        'form': form,
        'item': item,
        'authors_select': authors_select,
    }
    
    return render(request, template, context)


@login_required
@staff_member_required
def delete_item(request, item_id):
    """
    Delete a database item: make 
    it active=False to maintain order history
    records. Hard delete is possible via admin.
    """

    item = get_object_or_404(Item, pk=item_id)

    item.campaign = None
    item.active = False
    item.save()
    messages.success(request, 'Product successfully deleted!')

    return redirect(reverse('items'))


@login_required
@staff_member_required
def create_campaign(request):
    """ Create a sales campaign """
    available = Item.objects.filter(campaign__isnull=True).filter(active=True)
    not_available = Item.objects.filter(
        campaign__isnull=False).filter(active=True)

    if request.method == "POST":
        form = CampaignForm(request.POST, request.FILES)
        included_items = request.POST.getlist('included_items')
        campaign_name = request.POST.get('campaign_name')
        # Check for existing campaign with same name
        check_name = Campaign.objects.filter(campaign_name=campaign_name)
        if check_name.exists():
            messages.error(
                request, 'Sorry, a campaign with this name already exists')
        else:
            # return reverse('create_campaign')
            form.save()
            for list_item in included_items:
                list_item = Item.objects.get(pk=list_item)
                list_item.campaign = Campaign.objects.get(
                    campaign_name=campaign_name)
                list_item.set_sale_price = request.POST.get('fixed_price')
                list_item.save()
            messages.success(request, 'Your campaign has been created.')
            return redirect('manage_campaigns')
    else:
        form = CampaignForm()

    available = available.filter(active=True)
    context = {
        'not_available': not_available,
        'available': available,
        'form': form,
    }

    return render(request, 'items/create_campaign.html', context)


@login_required
@staff_member_required
def manage_campaigns(request):
    """ View existing campaigns """

    campaigns = Campaign.objects.all().order_by('campaign_name')

    context = {
        'campaigns': campaigns,
    }

    return render(request, 'items/manage_campaigns.html', context)


@login_required
@staff_member_required
def deactivate_campaign(request, campaign_id):
    """ 
    Disable a campaign, without deleting it.
    Included products will remain unavailable for inclusion in other campaigns
    """

    campaign = get_object_or_404(Campaign, pk=campaign_id)
    included_items = Item.objects.filter(campaign__pk=campaign_id)
    for item_instance in included_items:
        item_instance.set_sale_price = 0.00
        item_instance.save()
    
    campaign.active = False
    campaign.save()
    
    messages.success(request, 'Campaign successfully deactivated')

    return redirect(reverse('manage_campaigns'))


@login_required
@staff_member_required
def activate_campaign(request, campaign_id):
    """ Enable an existing campaign """

    campaign = get_object_or_404(Campaign, pk=campaign_id)
    included_items = Item.objects.filter(campaign__pk=campaign_id)
    for item_instance in included_items:
        item_instance.set_sale_price = campaign.fixed_price
        item_instance.save()

    campaign.active = True
    campaign.save()

    messages.success(request, 'Campaign successfully activated')

    return redirect(reverse('manage_campaigns'))

@login_required
@staff_member_required
def update_campaign(request, campaign_id):
    """ Update an existing campaign """
    
    campaign = get_object_or_404(Campaign, pk=campaign_id)
    available = Item.objects.filter(campaign__isnull=True).filter(active=True)
    # List of included items to compare against
    original_inclusion_list = campaign.item_set.all()
    not_available_list = Item.objects.filter(
        campaign__isnull=False).filter(active=True)
    not_available = not_available_list.difference(original_inclusion_list)
    
    if request.method == "POST":
        form = CampaignForm(request.POST, request.FILES, instance=campaign)
        form.save()
        included_items = request.POST.getlist('included_items')
        already_included = request.POST.getlist('already_included')
        new_list = included_items + already_included
        # Clear campaign's included items to compile new list
        old_campaign_items = Item.objects.filter(campaign__pk=campaign_id)
        for item in old_campaign_items:
            item.campaign = None
            item.save()
        current_campaign = Campaign.objects.get(pk=campaign_id)
        fixed_price = request.POST.get('fixed_price')
        for list_item in new_list:
            list_item = Item.objects.get(pk=list_item)
            list_item.campaign = current_campaign
            list_item.set_sale_price = fixed_price
            list_item.save()
        
        messages.success(request, 'Campaign successfully updated.')
        return redirect('manage_campaigns')
        
    else:
        form = CampaignForm(instance=campaign)

    available = available.filter(active=True)
    context = {
        'original_inclusion_list': original_inclusion_list,
        'not_available': not_available,
        'available': available,
        'form': form,
        'campaign': campaign
    }
    
    return render(request, 'items/update_campaign.html', context)


@login_required
@staff_member_required
def delete_campaign(request, campaign_id):
    """ Delete a campaign """
    # Clear included items' association to campaign
    old_campaign_items = Item.objects.filter(campaign__pk=campaign_id)
    for item in old_campaign_items:
        item.campaign = None
        item.save()

    campaign = get_object_or_404(Campaign, pk=campaign_id)
    # Delete campaign itself
    campaign.delete()
    messages.success(request, 'Campaign successfully deleted.')

    return redirect(reverse('manage_campaigns'))
