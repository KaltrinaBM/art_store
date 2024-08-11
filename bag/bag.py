from decimal import Decimal
from django.conf import settings
from paintings.models import Painting


class Bag:
    def __init__(self, request):
        self.session = request.session
        bag = self.session.get(settings.BAG_SESSION_ID)
        if not bag:
            bag = self.session[settings.BAG_SESSION_ID] = {}
        self.bag = bag

    def add(self, painting, quantity=1, override_quantity=False):
        painting_id = str(painting.id)
        if painting_id not in self.bag:
            self.bag[painting_id] = {'quantity': 0, 'price': str(painting.price)}
        if override_quantity:
            self.bag[painting_id]['quantity'] = quantity
        else:
            self.bag[painting_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, painting):
        painting_id = str(painting.id)
        if painting_id in self.bag:
            del self.bag[painting_id]
            self.save()

    def __iter__(self):
        painting_ids = self.bag.keys()
        paintings = Painting.objects.filter(id__in=painting_ids)
        for painting in paintings:
            self.bag[str(painting.id)]['painting'] = painting

        for item in self.bag.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.bag.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.bag.values())

    def clear(self):
        del self.session[settings.BAG_SESSION_ID]
        self.save()
