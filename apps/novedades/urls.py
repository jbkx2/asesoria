from django.urls import include, path 
from rest_framework import routers 
from .views import NovedadViewSet, IndexView

router = routers.DefaultRouter()
router.register('novedades', NovedadViewSet)

urlpatterns = [
	path('api/', include(router.urls)),
	path('', IndexView.as_view(), name="index"),
]
