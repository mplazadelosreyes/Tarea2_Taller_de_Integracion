from .models import Hamburguesa, Ingrediente
from rest_framework import serializers

URL = "https://mariplahamburguesas.herokuapp.com/ingrediente"


class HamburguesaSerializer(serializers.ModelSerializer):

    ingredientes = serializers.SerializerMethodField()

    def get_ingredientes(self, ingredientes):
        ingredientes_paths = []
        lista = ingredientes.ingredientes.all()
        for elem in lista:
            ingredientes_paths.append({'path': URL + "{}".format(elem.id)})
        return ingredientes_paths

    class Meta:
        model = Hamburguesa
        fields = ['id', 'nombre', 'descripcion', 'precio', 'imagen', 'ingredientes']


class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre', 'descripcion']



