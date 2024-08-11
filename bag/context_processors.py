from .utils import get_bag_items


def bag_items_processor(request):
    return get_bag_items(request)
