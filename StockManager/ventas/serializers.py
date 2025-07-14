from rest_framework import serializers
from .models import Proveedor, Producto, Categoria, Venta, Cliente

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'phone', 'ruc']
    
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'price', 'stock', 'proveedor']
    
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['categoria_name', 'description', 'productos_categoria']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['producto_vendido', 'descuento', 'fecha']
        read_only_fields = ('fecha', )

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre_cliente', 'dni', 'compra']