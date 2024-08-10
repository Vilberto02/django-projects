from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Venta)
admin.site.register(Cliente)
admin.site.register(Cliente_Venta)
admin.site.register(Venta_Producto)
