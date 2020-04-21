from django.db import models
# Create your models here.


class Ingrediente(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()


class Hamburguesa(models.Model):
    nombre = models.TextField()
    precio = models.PositiveIntegerField()
    descripcion = models.TextField()
    imagen = models.TextField()
    ingredientes = models.ManyToManyField(Ingrediente, blank=True)

    #python manage.py makemigrations burgerapp