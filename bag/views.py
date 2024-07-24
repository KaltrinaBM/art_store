from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from paintings.models import Painting 
from django.http import JsonResponse

def update_icon_count(request):
    """ Update the count displayed on the bag icon """
    bag = request.session.get('bag', {})
    count = sum(bag.values())
    return JsonResponse({'count': count})

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')



def add_to_bag(request, item_id):
    """ Add a quantity of the specified painting to the shopping bag """
    painting = get_object_or_404(Painting, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    messages.success(request, f'Added {painting.title} to your bag')
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified painting to the specified amount"""
    painting = get_object_or_404(Painting, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    messages.success(
        request, f'Updated {painting.title} quantity to {bag.get(item_id, 0)}'
    )
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    painting = get_object_or_404(Painting, pk=item_id)
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag.pop(item_id)
        messages.success(request, f'Removed {painting.title} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
