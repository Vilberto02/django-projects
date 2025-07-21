from django.shortcuts import render
from .models import Proveedor, Producto, Categoria, Venta, Cliente
from rest_framework import viewsets, permissions
from .serializers import (
    ProveedorSerializer,
    ProductoSerializer,
    CategoriaSerializer,
    VentaSerializer,
    ClienteSerializer,
)


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all().order_by("datos_proveedor")
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by("nombre_producto")
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by("nombre_categoria")
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all().order_by("producto_vendido")
    permission_classes = [permissions.AllowAny]
    serializer_class = VentaSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by("datos_cliente")
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer
