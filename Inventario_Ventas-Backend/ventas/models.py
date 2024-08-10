from django.db import models

# Create your models here.

class Proveedor(models.Model):
  nombre = models.CharField( max_length=300,verbose_name="Nombre")
  telefono = models.PositiveIntegerField(verbose_name="Telefono")
  ruc = models.PositiveIntegerField(verbose_name="RUC")

class Categoria(models.Model):
  nombre = models.CharField(max_length=300,verbose_name="Nombre")
  descripcion = models.TextField(verbose_name="Descripcion")

class Producto(models.Model):
  nombre = models.CharField(max_length=400, verbose_name="Nombre")
  precio = models.FloatField(verbose_name="Precio")
  stock = models.PositiveIntegerField(verbose_name="Stock")
  proveedor_id = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
  categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Venta(models.Model):
  descuento = models.FloatField(verbose_name="Descuento")
  fecha = models.DateTimeField(verbose_name="Fecha")

class Venta_Producto(models.Model):
  venta_id = models.ForeignKey(Venta, on_delete=models.CASCADE,verbose_name="ID Venta")
  producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="ID Producto")

class Cliente(models.Model):
  nombre = models.CharField(max_length=500,verbose_name="Nombre")
  dni = models.PositiveIntegerField(verbose_name="DNI")

class Cliente_Venta(models.Model):
  cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="ID Cliente")
  venta_id = models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name="ID Venta")