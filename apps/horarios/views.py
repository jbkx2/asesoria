from rest_framework import viewsets
from rest_framework.permissions import BasePermission, DjangoModelPermissions, SAFE_METHODS

from .serializers import TurnoSerializer
from .models import Turno 

class TurnoViewSet(viewsets.ModelViewSet):
	queryset = Turno.objects.all()
	serializer_class = TurnoSerializer
	