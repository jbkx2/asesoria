from rest_framework import viewsets
from rest_framework.permissions import BasePermission, DjangoModelPermissions, SAFE_METHODS
from django.views.generic import TemplateView

from .serializers import NovedadSerializer
from .models import Novedad

class NovedadViewSet(viewsets.ModelViewSet):
	queryset = Novedad.objects.all()
	serializer_class = NovedadSerializer

class IndexView(TemplateView):
	template_name = 'index.html'
