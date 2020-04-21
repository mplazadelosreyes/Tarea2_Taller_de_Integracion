from .models import Hamburguesa, Ingrediente
from rest_framework import serializers


class HamburguesaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hamburguesa
        fields = ['id', 'nombre', 'descripcion', 'precio', 'imagen', 'ingredientes']


class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre', 'descripcion']