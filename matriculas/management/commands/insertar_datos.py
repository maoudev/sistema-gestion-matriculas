from typing import Any
from django.core.management.base import BaseCommand

from matriculas.models import Periodo, Nacionalidad, Sala, Curso, Funcionario
from matriculas.utils import hash_password


class Command(BaseCommand):
    help = 'Insertar usuarios por defecto'
    
    def handle(self, *args: Any, **options: Any) -> str | None:
                
        funcionarios = [
            Funcionario(rut='12345678-9', nombres='Juan', paterno='Perez', materno='Gonzalez', correo='juan.perez@gmail.com', cargo='docente', asignatura='Matematicas', jefatura=True, password=hash_password('docente123')),
            Funcionario(rut='11222333-4', nombres='David', paterno='Silva', materno='Díaz', correo='david.silva@gmail.com', cargo='admin', jefatura=False, password=hash_password('admin123')),
        ]
        salas = []
        for i in range(200, 250):
            salas.append(Sala(numero = i))

        Sala.objects.bulk_create(salas)
        self.stdout.write(self.style.SUCCESS('Salas insertadas correctamente'))
        


        funcionarios = [
            Funcionario(rut='12345678-9', nombres='Juan', paterno='Perez', materno='Gonzalez', correo='juan.perez@gmail.com', cargo='docente', asignatura='Matematicas', jefatura=True, password=hash_password('docente123')),
            Funcionario(rut='11222333-4', nombres='David', paterno='Silva', materno='Díaz', correo='david.silva@gmail.com', cargo='admin', jefatura=False, password=hash_password('admin123')),
        ]

        Funcionario.objects.bulk_create(funcionarios)
        self.stdout.write(self.style.SUCCESS('Funcionarios insertados correctamente'))

        periodos = (
            Periodo(anio = 2024, activo = True),
        )

        Periodo.objects.bulk_create(periodos)
        self.stdout.write(self.style.SUCCESS('Periodos insertados correctamente'))

        nacionalidades = (
            Nacionalidad(nombre = 'Chilena'),
            Nacionalidad(nombre = 'Argentina'),
            Nacionalidad(nombre = 'Peruana'),
            Nacionalidad(nombre = 'Boliviana'),
            Nacionalidad(nombre = 'Colombiana'),
            Nacionalidad(nombre = 'Ecuatoriana'),
            Nacionalidad(nombre = 'Venezolana'),
            Nacionalidad(nombre = 'Uruguaya'),
            Nacionalidad(nombre = 'Paraguaya'),
            Nacionalidad(nombre = 'Brasileña'),
            Nacionalidad(nombre = 'Mexicana'),
            Nacionalidad(nombre = 'Española'),
        )

        sala = Sala.objects.get(numero=200)
        profesor_jefe = Funcionario.objects.get(rut='12345678-9')

        periodo = Periodo.objects.get(anio=2024)
        cursos = (
            Curso(nombre = '1A', profesor_jefe = profesor_jefe, sala = sala, periodo = periodo),
        )

        Curso.objects.bulk_create(cursos)
        self.stdout.write(self.style.SUCCESS('Cursos insertados correctamente'))

        curso = Curso.objects.get(nombre='1A')
        curso.profesores.add(profesor_jefe)
        self.stdout.write(self.style.SUCCESS('Docente asignado correctamente'))


        Nacionalidad.objects.bulk_create(nacionalidades)
        self.stdout.write(self.style.SUCCESS('Nacionalidades insertadas correctamente'))

