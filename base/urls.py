from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='homepage'),
	path('mentions-legales', views.mentions_legales, name='mentions_legales'),
	path('politique-de-confidentialite-des-donnees', views.confidentialite_donnees, name='confidentialite_donnees'),
	path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain'), name='robots.txt'),
]