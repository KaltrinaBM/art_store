from django.db import models
from django.contrib.auth.models import User


# Model for Blog Posts Category and Tags
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# Model for Tags on Blog Posts
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model for Blog Posts with details
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    excerpt = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='blog_images/',
        blank=True,
        null=True
        )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
