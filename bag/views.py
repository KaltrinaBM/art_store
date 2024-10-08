from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404
)
from django.contrib import messages
from paintings.models import Painting
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def update_icon_count(request):
    """ Update the count displayed on the bag icon """
    bag = request.session.get('bag', {})
    count = sum(bag.values())
    return JsonResponse({'count': count})


def view_bag(request):
    bag = request.session.get('bag', {})
    bag_items = []
    total_price = 0

    for item_id, item_data in bag.items():
        painting = get_object_or_404(Painting, pk=item_id)
        quantity = item_data
        item_total_price = quantity * painting.price
        total_price += item_total_price
        bag_items.append({
            'item_id': item_id,
            'painting': painting,
            'quantity': quantity,
            'total_price': item_total_price,
        })

    context = {
        'bag_items': bag_items,
        'total_price': total_price,
    }
    return render(request, 'bag/bag.html', context)


@require_POST
def add_to_bag(request, item_id):
    painting = get_object_or_404(Painting, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id] += quantity
        messages.success(
            request,
            f'Updated {painting.title} quantity to {bag[item_id]}'
            )

    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {painting.title} to your bag')

    request.session['bag'] = bag

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'count': sum(bag.values())})

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    painting = get_object_or_404(Painting, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated {painting.title} quantity to {bag[item_id]}'
            )

    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {painting.title} from your bag')

    request.session['bag'] = bag
    return JsonResponse({'success': True})


def remove_from_bag(request, item_id):
    painting = get_object_or_404(Painting, pk=item_id)
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag.pop(item_id)
        messages.success(request, f'Removed {painting.title} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
