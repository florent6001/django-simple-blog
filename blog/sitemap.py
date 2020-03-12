from django.contrib.sitemaps import Sitemap
from blog.models import Post, Category

class PostSitemap(Sitemap):
	
	def items(self):
		return Post.objects.all()

class CategorySitemap(Sitemap):
	
	def items(self):
		return Category.objects.all()