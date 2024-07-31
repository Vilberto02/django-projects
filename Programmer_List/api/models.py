from django.db import models

# Create your models here.
class Programmer(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="Nombres")
    nickname = models.CharField(max_length=50, verbose_name="Username")
    age = models.PositiveSmallIntegerField(verbose_name="Edad")
    is_activate = models.BooleanField(verbose_name="¿Esta activo?")

class Designer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombres")
    username = models.CharField(max_length=50, verbose_name="Username")
    age = models.PositiveSmallIntegerField(verbose_name="Edad")
    is_activate = models.BooleanField(verbose_name="¿Esta activo?")