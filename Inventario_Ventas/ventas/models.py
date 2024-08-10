from django.db import models
# Create your models here.


class Proveedor(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    phone = models.PositiveIntegerField(
        verbose_name="Telefono", blank=True, null=True)
    ruc = models.PositiveIntegerField(
        verbose_name="RUC", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre_producto = models.CharField(
        max_length=200, verbose_name="Nombre del producto", null=True)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Precio", null=True)
    stock = models.PositiveIntegerField(
        verbose_name="Stock")
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.CASCADE, verbose_name="Proveedor", null=True)

    class Meta:
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre_producto


class Categoria(models.Model):
    categoria_name = models.CharField(
        max_length=200, verbose_name="Nombre de la categoria", null=True)
    description = models.TextField(verbose_name="Descripcion")
    productos_categoria = models.ForeignKey(
        Producto, on_delete=models.CASCADE, verbose_name="Categoria del producto", null=True)

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.categoria_name


class Venta(models.Model):
    producto_vendido = models.ForeignKey(
        Producto, on_delete=models.CASCADE, verbose_name="Producto vendido", null=True)
    descuento = models.DecimalField(
        max_digits=3, decimal_places=2, verbose_name="Descuento")
    fecha = models.DateTimeField(auto_now=True, verbose_name="Fecha")

    class Meta:
        verbose_name_plural = "Ventas"

    def __str__(self):
        return f"{self.producto_vendido}"


class Cliente(models.Model):
    nombre_cliente = models.CharField(
        max_length=200, verbose_name="Nombre del cliente", null=True)
    dni = models.PositiveIntegerField(verbose_name="DNI")
    compra = models.ForeignKey(
        Venta, on_delete=models.CASCADE, verbose_name="Producto comprado", null=True)

    class Meta:
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre_cliente
