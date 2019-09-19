from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from myblog.sitemaps import PostSitemap
from django.conf.urls.static import static
from django.conf import settings


sitemaps = {
	'posts': PostSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myblog.urls', namespace='myblog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name = 'django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)