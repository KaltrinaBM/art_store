import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from paintings.models import Painting

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=40)
    town_or_city = models.CharField(max_length=40)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order {self.id} by {self.full_name}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.painting.title}'
