from typing import Any
from django.core.management.base import BaseCommand

from matriculas.models import Usuario
from matriculas.utils import hash_password


class Command(BaseCommand):
    help = 'Insertar usuarios por defecto'
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        usuarios = (
            Usuario(nombre='admin', password=hash_password('admin123'), tipo='admin'),
            Usuario(nombre='funcionario', password=hash_password('funcionario123'), tipo='funcionario'),
            Usuario(nombre='docente', password=hash_password('docente123'), tipo='docente'),
        )

        Usuario.objects.bulk_create(usuarios)
        self.stdout.write(self.style.SUCCESS('Usuarios insertados correctamente'))


