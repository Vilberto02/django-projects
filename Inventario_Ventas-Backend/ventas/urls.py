from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()

router.register(r'Proveedor', ProveedorViewSet)
router.register(r'Producto', ProductoViewSet)
router.register(r'Categoria', CategoriaViewSet)
router.register(r'Venta', VentaViewSet)
router.register(r'Cliente', ClienteViewSet)
router.register(r'Cliente_Venta', Cliente_VentaViewSet)
router.register(r'Venta_Producto', Venta_ProductoViewSet)

urlpatterns = [
  path('', include(router.urls)),
]