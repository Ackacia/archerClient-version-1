from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from servicesEval.views import dashboard

admin.site.site_header = "L'Archer-Capital Administration"
admin.site.site_title = "L'Archer Capital"
admin.site.index_title = "Bienvenue dans l'administration L'Archer Capital"


urlpatterns = [
    path("", dashboard, name='dash'),
    path('admin/', admin.site.urls),
    path('cover-rencontre-elle/', include('coverRencontre.urls')),
    path('service-evaluation/', include('servicesEval.urls')),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, )

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)