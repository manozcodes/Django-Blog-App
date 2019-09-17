from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myblog.urls', namespace='myblog')),
]