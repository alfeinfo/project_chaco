from django.db import models


# Create your models here.

class Jugador(models.Model):
	nombre = models.charfield(max_length= 255)
	apellido= models.charfield(max_length=255)
	edad = models.datefield(max_length= 255)

	def nombre_apellido(self):
		cadena== "(0), (1)"
		return cadena.format(self.nombre,self.apellido)

	def __str__(self):
		return self.nombre_apellido()

	class usuarios (models.Model)
	nombre = models.charfield(max_length=255)
	
