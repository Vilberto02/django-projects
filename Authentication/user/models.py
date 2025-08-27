from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
  nombres = models.CharField(verbose_name="Nombres")
  apellidos = models.CharField(verbose_name="Apellidos")
  nombre_usuario = models.CharField(verbose_name="Nombre de usuario")
  correo_electronico = models.CharField(verbose_name="Correo electrónico")
  contrasena = models.CharField(verbose_name="Contrseña")