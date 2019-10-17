from django.contrib import admin
from .models import Novedad

@admin.register(Novedad)
class NovedadAdmin(admin.ModelAdmin):
	model = Novedad
	list_filter = ['titulo']
	search_fields = ['titulo']
