from django.db import models

# Create your models here.
class Programador(models.Model):
    datos_programador = models.CharField(max_length=100, verbose_name="Nombres y apellidos")
    nombre_usuario = models.CharField(max_length=50, verbose_name="Nombre de usuario")
    edad = models.PositiveSmallIntegerField(verbose_name="Edad")
    esta_activo = models.BooleanField(verbose_name="¿Esta activo?")

    class Meta:
      verbose_name = "Programador"
      verbose_name_plural = "Programadores"

    def __str__(self):
      return self.nombre_usuario

class Disenador(models.Model):
    datos_disenador = models.CharField(max_length=100, verbose_name="Nombres y apellidos")
    nombre_usuario = models.CharField(max_length=50, verbose_name="Nombre de usuario")
    edad = models.PositiveSmallIntegerField(verbose_name="Edad")
    esta_activo = models.BooleanField(verbose_name="¿Esta activo?")

    class Meta:
      verbose_name = "Diseñador"
      verbose_name_plural = "Diseñadores"

    def __str__(self):
      return self.nombre_usuario