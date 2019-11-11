from django.db import models

class Novedad(models.Model):

	titulo = models.CharField(max_length=60, help_text='Obligatorio')
	fecha_pub = models.DateField('Ingrese Fecha de Publicacion')
	desc = models.CharField(max_length=200)
	contenido = models.TextField(max_length=600)
	imagen = models.ImageField(upload_to='asesoria/apps/novedades' ,help_text='Opcional', blank=True, null=True)

	def __str__(self):
		return '%s, %s' % (self.titulo, self.fecha_pub)

	class Meta():
		ordering = ['fecha_pub']
		verbose_name_plural = 'noticias'