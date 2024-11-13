from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.TextField(max_length=50)
    password = models.TextField(max_length=50)
    tipo = models.TextField(max_length=50)
    estado = models.BooleanField(default=True)
    cantidad_intentos = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.nombre}-{self.password}-{self.tipo}-{self.estado}-{self.cantidad_intentos}'