from rest_framework import serializers
from .models import Novedad

class NovedadSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Novedad 
		fields = ('titulo', 'texto', 'imagen')
