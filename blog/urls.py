from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='blog_index'),
	path('categorie/<slug>', views.show_category, name='show_category'),
	path('<slug>', views.show_post, name='show_post')
]