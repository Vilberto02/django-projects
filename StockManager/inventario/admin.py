from django.contrib import admin
from .models import Proveedor, Producto, Categoria, Venta, Cliente

# Register your models here.


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("datos_proveedor", "numero_telefono", "numero_ruc")
    search_fields = ("datos_proceedor",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_producto",
        "precio_producto",
        "cantidad_producto",
        "proveedor_producto",
        "categoria_producto",
    )
    list_filter = ("proveedor_producto", "categoria_producto")
    search_fields = ("nombre_producto",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre_categoria", "descripcion_categoria")
    search_fields = ("nombre_categoria",)


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ("producto_vendido", "descuento_venta", "fecha_venta")


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        "datos_cliente",
        "tipo_documento",
        "numero_identidad",
        "compra_cliente",
    )
    list_filter = ("tipo_documento",)
