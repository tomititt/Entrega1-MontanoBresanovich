from django.db import models

# Create your models here.

class Asignatura(models.Model):

    nombre = models.CharField(max_length=40)
    clase = models.IntegerField()

class Mago(models.Model):

    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    casa = models.CharField(max_length=40)

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    materia = models.CharField(max_length=60)

class Extasis(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    aprobado = models.BooleanField()
