import uuid
from django.db import models


class Ingrediente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #uuid
    nombre = models.CharField()
    descripcion = models.CharField()


# Create your models here.
class Hamburguesa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField()
    precio = models.PositiveIntegerField()
    descripcion = models.CharField()
    imagen = models.ImageField()
    ingredientes = models.ManyToManyField(Ingrediente)
    #falta aca pa juntarlo (burger con ingrediente)
    #ingredientes = [paths de los ingredientes onda mariplaapp/ingrediete/1 #url]
    #tengo que hacer la migracion parte 2 del tutorial
    #python manage.py makemigrations burgerapp