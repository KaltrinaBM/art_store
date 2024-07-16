from django.contrib import admin
from .models import Painting

class PaintingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

    ordering = ('sku',)

    search_fields = ('title', 'description')

admin.site.register(Painting, PaintingAdmin)
