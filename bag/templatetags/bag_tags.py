from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    """ Custom filter to get an item from a dictionary by key """
    return dictionary.get(key)

@register.simple_tag
def bag_count(request):
    """ Custom tag to get the count of items in the bag """
    bag = request.session.get('bag', {})
    return sum(quantity for quantity in bag.values())
