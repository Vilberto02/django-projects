from .models import *
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Producto
    fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Proveedor
    fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Categoria
    fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Venta
    fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cliente
    fields = '__all__'

class Cliente_VentaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cliente_Venta
    fields = '__all__'

class Venta_ProductoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Venta_Producto
    fields = '__all__'