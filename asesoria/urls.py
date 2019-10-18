from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('horarios/', include('apps.horarios.urls')),
    path('novedades/', include('apps.novedades.urls'))
]
