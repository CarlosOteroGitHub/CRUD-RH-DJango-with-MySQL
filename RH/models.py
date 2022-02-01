from django.db import models

# Create your models here.
class Empleado(models.Model):

	id_empleado = models.IntegerField(primary_key=True, max_length=5)
	nombre = models.CharField(max_length=100)
	nacimiento = models.DateField()
	correo = models.TextField(max_length=100)
	descripcion = models.TextField(max_length=100, null=True)

	def __str__(self):
		texto = "{0} ({1})"
		return texto.format(self.nombre, self.nacimiento, self.correo, self.descripcion)