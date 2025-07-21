from rest_framework import serializers
from .models import Proveedor, Producto, Categoria, Venta, Cliente


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ["datos_proveedor", "numero_telefono", "numero_ruc"]


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            "nombre_producto",
            "precio_producto",
            "cantidad_producto",
            "proveedor_producto",
            "categoria_producto",
        ]


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["nombre_categoria", "descripcion_categoria"]


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ["producto_vendido", "descuento_venta", "fecha_venta"]
        read_only_fields = ("fecha",)


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            "datos_cliente",
            "tipo_documento",
            "numero_identidad",
            "compra_cliente",
        ]
