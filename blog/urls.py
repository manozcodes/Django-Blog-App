from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from myblog.sitemaps import PostSitemap

sitemaps = {
	'posts': PostSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myblog.urls', namespace='myblog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name = 'django.contrib.sitemaps.views.sitemap'),
]