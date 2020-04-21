from rest_framework import viewsets
from django.shortcuts import render

from .models import Hamburguesa
from .models import Ingrediente

from rest_framework import permissions
from .serializer import IngredienteSerializer, HamburguesaSerializer


# Create your views here.
class HamburguesaViewSet(viewsets.ModelViewSet):
    queryset = Hamburguesa.objects.all()
    serializer_class = HamburguesaSerializer


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer