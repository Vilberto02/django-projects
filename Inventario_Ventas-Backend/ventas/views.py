from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, permissions

# Create your views here.
class ProveedorViewSet(viewsets.ModelViewSet):
  queryset = Proveedor.objects.all()
  serializer_class = ProveedorSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
  queryset = Categoria.objects.all()
  serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
  queryset = Producto.objects.all()
  serializer_class = ProductoSerializer

class VentaViewSet(viewsets.ModelViewSet):
  queryset = Venta.objects.all()
  serializer_class = VentaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
  queryset = Cliente.objects.all()
  serializer_class = ClienteSerializer

class Cliente_VentaViewSet(viewsets.ModelViewSet):
  queryset = Cliente_Venta.objects.all()
  serializer_class = Cliente_VentaSerializer

class Venta_ProductoViewSet(viewsets.ModelViewSet):
  queryset = Venta_Producto.objects.all()
  serializer_class = Venta_ProductoSerializer