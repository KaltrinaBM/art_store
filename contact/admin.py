from django.contrib import admin
from .models import ContactMessage
from django_summernote.admin import SummernoteModelAdmin

@admin.register(ContactMessage)
class ContactMessageAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    summernote_fields = ('message',)
