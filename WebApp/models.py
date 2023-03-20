from django.db import models

# Create your models here.
class Estudiante(models.Model):
    # Clase estudiante, Nombre, Apellido y a que camada pertenece
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f'Estudiante: {self.nombre} {self.apellido}, Camada: {self.camada}'

class Profesor(models.Model):
    # Clase de Profesor, Nombre y Apellido y Curso que Ensenia
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    cursos = models.CharField(max_length=40)

    def __str__(self):
        return f'Profesor: {self.nombre} {self.apellido}, Cursos: {self.cursos}'

class Curso(models.Model):
    # Clase Curso, con nombre y Camada
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField(unique=True)

    def __str__(self):
        return f'Curso: {self.nombre}, Camada: {self.camada}'