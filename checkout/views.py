from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from paintings.models import Painting

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('paintings'))

    order_form = OrderForm()
    
    # Calculate painting_count, total, and grand_total
    bag_items = []
    painting_count = 0
    total = 0
    for item_id, quantity in bag.items():
        painting = get_object_or_404(Painting, pk=item_id)
        subtotal = painting.price * quantity
        total += subtotal
        painting_count += quantity
        bag_items.append({
            'painting': painting,
            'quantity': quantity,
            'subtotal': subtotal,
        })
    grand_total = total  # Adjust as needed

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'bag_items': bag_items,
        'painting_count': painting_count,
        'total': total,
        'grand_total': grand_total,
    }

    return render(request, template, context)
