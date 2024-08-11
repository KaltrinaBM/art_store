from django.contrib import admin
from .models import Review


#Reviews from admin side
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'painting', 'rating', 'created_at', 'updated_at')
    search_fields = ('user__username', 'painting__title', 'content')

admin.site.register(Review, ReviewAdmin)
