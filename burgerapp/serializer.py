from .models import Hamburguesa, Ingrediente
from rest_framework import serializers

URL = "http://127.0.0.1:8000/ingrediente/"


class HamburguesaSerializer(serializers.ModelSerializer):

    ingredientes = serializers.SerializerMethodField()

    def get_ingredientes(self, ingredientes):
        ingrediente_path = URL + "{}".format(ingredientes.id)
        return ingrediente_path

    class Meta:
        model = Hamburguesa
        fields = ['id', 'nombre', 'descripcion', 'precio', 'imagen', 'ingredientes']


class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre', 'descripcion']