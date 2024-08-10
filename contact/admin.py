from django.contrib import admin
from .models import ContactMessage
from django_summernote.admin import SummernoteModelAdmin


# #Admin class for managing Post objects.
# @admin.register(Post)
# class PostAdmin(SummernoteModelAdmin):

#     list_display = ('title', 'slug', 'status', 'created_on')
#     search_fields = ['title', 'content']
#     list_filter = ('status', 'created_on',)
#     prepopulated_fields = {'slug': ('title',)}
#     summernote_fields = ('content',)


#Admin class for managing ContactFormEntry objects.
@admin.register(ContactMessage)
class ContactMessageAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    summernote_fields = ('message',)
