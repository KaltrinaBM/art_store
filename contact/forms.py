from django import forms
from .models import ContactMessage


#Contact Form for site users to send messages to site owners
class ContactForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave empty")

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        error_messages = {
            'name': {
                'required': "Please enter your name.",
            },
            'email': {
                'required': "Please enter your email address.",
                'invalid': "Please enter a valid email address.",
            },
            'subject': {
                'required': "Please enter the subject.",
            },
            'message': {
                'required': "Please enter your message.",
            },
        }
