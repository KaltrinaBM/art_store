from django.contrib import admin
from .models import BlogPost, Category, Tag
from django_summernote.admin import SummernoteModelAdmin


# Admin configuration for the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Admin configuration for the Tag model
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

    actions = ['merge_tags']

    # Delete selected tags
    def delete_selected_tags(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"Successfully deleted {count} tags.")
    delete_selected_tags.short_description = "Delete selected tags"

    # Merges selected tags into the first selected tag
    def merge_tags(self, request, queryset):

        if queryset.count() > 1:
            primary_tag = queryset.first()
            other_tags = queryset[1:]

            for tag in other_tags:
                tag.merge_into(primary_tag)
            self.message_user(request, f"Tags merged into {primary_tag.name}.")
    merge_tags.short_description = "Merge selected tags"


# Admin configuration for the BlogPost model with Summernote integration
@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'created_at',
        'updated_at'
    )
    search_fields = (
        'title',
        'content',
        'author__username',
        'category__name',
        'tags__name'
    )
    list_filter = (
        'created_at',
        'updated_at',
        'author',
        'category',
        'tags'
    )
    ordering = ('-created_at',)
    fields = (
        'title',
        'author',
        'content',
        'excerpt',
        'image',
        'category',
        'tags'
    )
    filter_horizontal = ('tags',)

    summernote_fields = ('content', 'excerpt')
