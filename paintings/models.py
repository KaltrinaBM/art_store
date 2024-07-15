from django.db import models

class Painting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='paintings/', null=True, blank=True)
    #sku = models.CharField(max_length=100, blank=True, default='') 

    def __str__(self):
        return self.title
