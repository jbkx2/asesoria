from django.urls import include, path 
from rest_framework import routers 
from .views import NovedadViewSet

router = routers.DefaultRouter()
router.register('novedades', NovedadViewSet)

urlpatterns = [
	path('', include(router.urls))
]
