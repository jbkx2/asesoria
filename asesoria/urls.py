from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('horarios/', include('apps.horarios.urls')),
    path('', include('apps.novedades.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
