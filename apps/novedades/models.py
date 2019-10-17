from django.db import models

class Novedad(models.Model):

	titulo = models.CharField(max_length=50, help_text='Obligatorio')
	texto = models.TextField(null=True, blank=True)
	imagen = models.ImageField(upload_to='asesoria/novedades' ,help_text='Opcional', blank=True, null=True)

	def __str__(self):
		return '%s' % (self.titulo)
