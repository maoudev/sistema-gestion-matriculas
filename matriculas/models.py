from django.db import models

    
class Funcionario(models.Model):
    rut = models.TextField(max_length=13)
    nombres = models.TextField(max_length=100)
    paterno = models.TextField(max_length=50)
    materno = models.TextField(max_length=50)
    correo = models.TextField(max_length=50)
    cargo = models.TextField(max_length=50)
    asignatura = models.TextField(max_length=100, null=True)
    jefatura = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)
    cantidad_intentos = models.IntegerField(default=0)
    password = models.TextField(max_length=50)



    def __str__(self):
        return f'{self.rut}-{self.nombres}-{self.paterno}-{self.materno}-{self.correo}-{self.cargo}-{self.asignatura}-{self.jefatura}-{self.estado}-{self.cantidad_intentos}-{self.password}'

class Sala(models.Model):
    numero = models.IntegerField()

    def __str__(self):
        return f'{self.numero}'

class Periodo(models.Model):
    anio = models.IntegerField(unique=True)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.anio}-{self.activo}'



class Curso(models.Model):
    nombre = models.TextField(max_length=50)
    profesor_jefe = models.ForeignKey(
        Funcionario, 
        on_delete=models.SET_NULL, 
        null=True, 
    )
    profesores = models.ManyToManyField(
        Funcionario, 
        related_name='cursos',
    )
    sala = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True)
    cantidad_alumnos = models.IntegerField(default=0)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, null=True)

    
    def __str__(self):
        return f'{self.nombre}-{self.profesor_jefe}-{self.sala}-{self.cantidad_alumnos}'


class Nacionalidad(models.Model):
    nombre = models.TextField(max_length=100)

    def __str__(self):
        return self.nombre


class Alumno(models.Model):
    rut = models.TextField(max_length=13)
    nombres = models.TextField(max_length=100)
    paterno = models.TextField(max_length=50)
    materno = models.TextField(max_length=50)
    edad = models.IntegerField()
    nacionalidades = models.ManyToManyField(Nacionalidad)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    promedio_anterior = models.IntegerField()

    def __str__(self):
        primera_nacionalidad = self.nacionalidades.first()
        nacionalidad_nombre = primera_nacionalidad.nombre if primera_nacionalidad else "Sin nacionalidad"
        return f'{self.nombres}-{self.paterno}-{self.materno}-{self.rut}-{self.curso}-{nacionalidad_nombre}'


class Apoderado(models.Model):
    rut = models.TextField(max_length=13)
    nombres = models.TextField(max_length=100)
    paterno = models.TextField(max_length=50)
    materno = models.TextField(max_length=50)
    edad = models.IntegerField()
    parentesco = models.TextField(max_length=50)
    nacionalidades = models.ManyToManyField(Nacionalidad)

    def __str__(self):
        primera_nacionalidad = self.nacionalidades.first()
        nacionalidad_nombre = primera_nacionalidad.nombre if primera_nacionalidad else "Sin nacionalidad"
        return f'{self.nombres}-{self.paterno}-{self.materno}-{self.rut}-{self.parentesco}-{nacionalidad_nombre}'


class Matricula(models.Model):
    apoderado = models.ForeignKey(Apoderado, on_delete=models.SET_NULL, null=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.SET_NULL, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.apoderado}-{self.alumno}-{self.curso}-{self.periodo}'
    


class RegistroAccion(models.Model):
    usuario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    accion = models.CharField(max_length=255)
    detalles = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.accion} - {self.fecha}"
