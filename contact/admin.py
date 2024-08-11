from django.contrib import admin
from .models import ContactMessage
from django_summernote.admin import SummernoteModelAdmin


#Admin for managing received messages
@admin.register(ContactMessage)
class ContactMessageAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    summernote_fields = ('message',)
