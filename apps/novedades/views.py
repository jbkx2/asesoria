from rest_framework import viewsets
from rest_framework.permissions import BasePermission, DjangoModelPermissions, SAFE_METHODS

from .serializers import NovedadSerializer
from .models import Novedad

class NovedadViewSet(viewsets.ModelViewSet):
	queryset = Novedad.objects.all()
	serializer_class = NovedadSerializer
