from django.db import models

# Create your models here.


class Proveedor(models.Model):
    datos_proveedor = models.CharField(
        max_length=200, verbose_name="Nombres y apellidos"
    )
    numero_telefono = models.PositiveIntegerField(
        verbose_name="Número de telefono", blank=True, null=True
    )
    numero_ruc = models.PositiveIntegerField(verbose_name="RUC", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.nombre


# El producto solo pertenece a una categoria.
class Categoria(models.Model):
    nombre_categoria = models.CharField(
        max_length=200, verbose_name="Nombre de la categoria", null=True
    )
    descripcion_categoria = models.TextField(verbose_name="Descripcion")

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.categoria_name


class Producto(models.Model):
    nombre_producto = models.CharField(
        max_length=200, verbose_name="Nombre del producto", null=True
    )
    precio_producto = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Precio", null=True
    )
    cantidad_producto = models.PositiveIntegerField(verbose_name="Cantidad")
    proveedor_producto = models.ForeignKey(
        Proveedor, on_delete=models.CASCADE, verbose_name="Proveedor", null=True
    )
    categoria_producto = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, verbose_name="Categoria", null=True
    )

    class Meta:
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre_producto


class Venta(models.Model):
    producto_vendido = models.ForeignKey(
        Producto, on_delete=models.CASCADE, verbose_name="Producto vendido", null=True
    )
    descuento_venta = models.DecimalField(
        max_digits=3, decimal_places=2, verbose_name="Descuento", default="0.0"
    )
    fecha_venta = models.DateTimeField(auto_now=True, verbose_name="Fecha de venta")

    class Meta:
        verbose_name_plural = "Ventas"

    def __str__(self):
        return f"{self.producto_vendido}"


DOCUMENTOS_IDENTIDAD = (
    ("DNI", "DNI"),
    ("EXTRANJERIA", "Carnet de Extranjeria"),
    ("PASAPORTE", "Pasaporte"),
)


class Cliente(models.Model):
    datos_cliente = models.CharField(
        max_length=200, verbose_name="Nombres y apellidos", null=True
    )
    tipo_documento = models.CharField(
        max_length=20,
        choices=DOCUMENTOS_IDENTIDAD,
        default="DNI",
        verbose_name="Tipo de documento",
    )
    numero_identidad = models.PositiveIntegerField(verbose_name="Numero de identidad")
    compra_cliente = models.ForeignKey(
        Venta, on_delete=models.CASCADE, verbose_name="Producto comprado", null=True
    )

    class Meta:
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre_cliente
