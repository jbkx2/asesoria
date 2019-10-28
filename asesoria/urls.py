from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('horarios/', include('apps.horarios.urls')),
    path('', include('apps.novedades.urls'))
]
