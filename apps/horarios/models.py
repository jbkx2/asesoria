from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Turno(models.Model):

	nombre = models.CharField(
		max_length=40, 
		help_text='Ingrese el nombre.'
	)

	apellido = models.CharField(
		max_length=40, 
		help_text='Ingrese el apellido.'
	)

	hora_1_inicio = models.TimeField(
		"Desde",
		null=True,
		blank=True,
		help_text='Ingrese el inicio de la primera hora.'
	)

	hora_1_fin = models.TimeField(
		"Hasta",
		null=True,
		blank=True,
		help_text='Ingrese el fin de la primera hora.'
	)

	hora_2_inicio = models.TimeField(
		"Desde",
		null=True,
		blank=True,
		help_text='Ingrese el inicio de la segunda hora.'
	)

	hora_2_fin = models.TimeField(
		"Hasta",
		null=True,
		blank=True,
		help_text='Ingrese el fin de la segunda hora.'
	)

	hora_3_inicio = models.TimeField(
		"Desde",
		null=True,
		blank=True,
		help_text='Ingrese el inicio de la tercer hora.'
	)

	hora_3_fin = models.TimeField(
		"Hasta",
		null=True,
		blank=True,
		help_text='Ingrese el fin de la tercer hora.'
	)

	hora_4_inicio = models.TimeField(
		"Desde",
		null=True,
		blank=True,
		help_text='Ingrese el inicio de la cuarta hora.'
	)

	hora_4_fin = models.TimeField(
		"Hasta",
		null=True,
		blank=True,
		help_text='Ingrese el fin de la cuarta hora.'
	)

	hora_5_inicio = models.TimeField(
		"Desde",
		null=True,
		blank=True,
		help_text='Ingrese el inicio de la quinta hora.'
	)

	hora_5_fin = models.TimeField(
		"Hasta",
		null=True,
		blank=True,
		help_text='Ingrese el fin de la quinta hora.'
	)

	class Meta:
		verbose_name='Turno'
		verbose_name_plural = "Turnos"

	def __str__(self):
		return '%s %s' % (self.nombre, self.apellido)


