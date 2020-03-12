from django.conf.urls import handler404
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap

from base.sitemap import StaticViewSitemap
from blog.sitemap import PostSitemap, CategorySitemap

sitemaps = {
	'static': StaticViewSitemap, 
	'posts': PostSitemap,
	'categories': CategorySitemap,
}

handler404 = 'base.views.custom_404'

urlpatterns = [
    path('', include('base.urls')),
    path('contact', include('contact.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps }),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)