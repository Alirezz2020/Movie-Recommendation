
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls',namespace='accounts')),  # your accounts app URLs

    path('', include('home.urls', namespace='home')),
    path('movies/', include('movies.urls', namespace='movies')),  #enter new apps here
    path('recommendations/', include('recommendations.urls', namespace='recommendations')),  #enter new apps here
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)