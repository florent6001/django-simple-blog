from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='Prénom', max_length=100)
    last_name = forms.CharField(label='Nom de famille', max_length=100)
    email = forms.EmailField(label='Adresse email')
    message = forms.CharField(label='Message', widget=forms.Textarea)