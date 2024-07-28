from django.shortcuts import get_object_or_404
from paintings.models import Painting

def get_bag_items(request):
    bag = request.session.get('bag', {})
    bag_items = []

    for item_id, item_data in bag.items():
        painting = get_object_or_404(Painting, pk=item_id)
        quantity = item_data
        total_price = quantity * painting.price
        bag_items.append({
            'item_id': item_id,
            'painting': painting,
            'quantity': quantity,
            'total_price': total_price,
        })

    total_price = sum(item['total_price'] for item in bag_items)

    return {'bag_items': bag_items, 'total_price': total_price}
