from django.db import models
from django.contrib.auth.models import User
from paintings.models import Painting  # Assuming the Painting model is in paintings.models

class Review(models.Model):
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # Assuming a rating out of 5
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.painting.title}'
