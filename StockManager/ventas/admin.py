from django.contrib import admin
from .models import Proveedor, Producto, Categoria, Venta, Cliente

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Venta)
admin.site.register(Cliente)