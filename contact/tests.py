from django.test import TestCase, Client
from django.urls import reverse

class ContactTest(TestCase):
    def setUp(self):
        client = Client()

    def test_display_contact_form(self):
        response = self.client.get(reverse('contact'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'contact.html')

    def test_send_contact_form_with_data(self):
        response = self.client.post(reverse('contact'), {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'test@gmail.com',
            'message': 'Hi all'
        })

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Votre message à été envoyé avec succès.')

    def test_send_contact_form_without_data(self):
        response = self.client.post(reverse('contact'), {
            'first_name': '',
            'last_name': '',
            'email': '',
            'message': ''
        })

        self.assertEquals(response.status_code, 200)
        self.assertNotContains(response, 'Votre message à été envoyé avec succès.')
        self.assertTemplateUsed(response, 'contact.html')