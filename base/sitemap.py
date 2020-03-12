from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):

	def items(self):
		return ['homepage', 'contact', 'legal_notice', 'privacy_policy']
		
	def location(self, item):
		return reverse(item)