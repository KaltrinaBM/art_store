from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Check the honeypot field
            if form.cleaned_data['honeypot']:
                # If honeypot is filled, ignore submission
                messages.error(request, 'Invalid submission.')
                return redirect('contact')
            
            form.save()
            return redirect('thank_you')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def thank_you_view(request):
    return render(request, 'contact/thank_you.html')
