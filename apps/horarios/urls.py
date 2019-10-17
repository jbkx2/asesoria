from django.urls import include, path 
from rest_framework import routers
from .views import TurnoViewSet

router = routers.DefaultRouter()
router.register('turnos', TurnoViewSet)

urlpatterns = [
	path('', include(router.urls))
]