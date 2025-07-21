from django.contrib import admin
from .models import Programador, Disenador
# Register your models here.

@admin.register(Programador)
class ProgramadorAdmin(admin.ModelAdmin):
  list_display = ("datos_programador", "nombre_usuario", "edad", "esta_activo")
  list_filter = ("esta_activo", )
  search_fields = ("nombre_usuario",)


@admin.register(Disenador)
class DisenadorAdmin(admin.ModelAdmin):
  list_display = ("datos_disenador", "nombre_usuario", "edad", "esta_activo")
  list_filter = ("esta_activo",)
  search_fields = ("nombre_usuario", )