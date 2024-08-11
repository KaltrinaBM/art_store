from django.db import models
import uuid
from cloudinary.models import CloudinaryField


class Painting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', default='paintings/placeholder.jpg')
    sku = models.CharField(max_length=8, unique=True,
                           default=uuid.uuid4().hex[:8])

    def __str__(self):
        return self.title
