from django.test import TestCase, Client
from django.urls import reverse

class baseTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.homepage = reverse('homepage')
        self.mentions_legales = reverse('mentions_legales')
        self.confidentialite_donnees = reverse('confidentialite_donnees')
        self.robots_txt = reverse('robots.txt')
        # Robots.txt

    def test_homepage_display(self):
        response = self.client.get(self.homepage)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')

    def test_mentions_legales_display(self):
        response = self.client.get(self.mentions_legales)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mentions_legales.html')

    def test_confidentialite_donnees_display(self):
        response = self.client.get(self.confidentialite_donnees)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'confidentialite_donnees.html')

    def test_robots_txt_display(self):
        response = self.client.get(self.robots_txt)
        self.assertEquals(response.status_code, 200)