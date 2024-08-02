import uuid
from django.db import models
from django.db.models import Sum
from paintings.models import Painting

class Order(models.Model):
    order_number = models.CharField(max_length=32, unique=True, blank=True)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """Generate a random, unique order number using UUID"""
        return str(uuid.uuid4().hex)[:32].upper()  # Ensure it is within 32 characters

    def update_total(self):
        """Update grand total each time a line item is added, without accounting for delivery costs as shipping is free."""
        self.order_total = self.items.aggregate(Sum('item_total'))['item_total__sum'] or 0
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """Override the original save method to set the order number if it hasn't been set already."""
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order {self.id} by {self.full_name}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='items')
    painting = models.ForeignKey(Painting, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0, editable=False)

    def save(self, *args, **kwargs):
        """Override the original save method to set the line item total and update the order total."""
        self.item_total = self.painting.price * self.quantity
        super().save(*args, **kwargs)
        self.order.update_total()

    def __str__(self):
        return f'SKU {self.painting.sku} x {self.order.order_number}'
