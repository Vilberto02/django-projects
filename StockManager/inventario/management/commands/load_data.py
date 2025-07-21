from django.core.management.base import BaseCommand

# Asegúrate de ajustar "tuapp" al nombre de tu aplicación
from ventas.models import Proveedor
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = "Carga datos de pisos y aulas en la base de datos"

    def handle(self, *args, **options):
        proveedores = [
            {"nombre": "Juan Velarde", "phone": 123456, "ruc": 123789},
            {"nombre": "Manuel Flores", "phone": 124567, "ruc": 789456},
            {"nombre": "Alberto Patricio", "phone": 456237, "ruc": 963741},
        ]

        for nombre_proveedores in proveedores:
            try:
                # Crea un objeto Piso en la base de datos
                piso, created = Proveedor.objects.get_or_create(
                    nombre=nombre_proveedores.get("nombre"),
                    phone=nombre_proveedores.get("phone"),
                    ruc=nombre_proveedores.get("ruc"),
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Se ha creado el piso: {nombre_proveedores}"
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f"El piso {nombre_proveedores} ya existe en la base de datos."
                        )
                    )

            except IntegrityError as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Error al crear el piso {nombre_proveedores}: {e}"
                    )
                )
