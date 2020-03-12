from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            plaintext = render_to_string('emails/contact.txt', {'data': data})
            html = render_to_string('emails/contact.html', {'data': data})

            send_mail(subject='Demande de contact', message=plaintext, html_message=html,
                      from_email=data['email'], recipient_list=[settings.CONTACT_EMAIL])

            messages.success(
                request, 'Votre message à été envoyé avec succès.')
        else:
            messages.error(request, 'Une erreur s\'est produite.')
    form = ContactForm()
    data = {'form': form}
    return render(request, 'contact.html', data)
