from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Hamburguesa
from .models import Ingrediente

from .serializer import IngredienteSerializer, HamburguesaSerializer


@api_view(['GET', 'POST'])
def hamburguesa_list(request):

    if request.method == 'GET':
        serializer_context = {
            'request': request,
        }
        snippets = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(snippets, context=serializer_context, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HamburguesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Hamburguesa creada",
                            status=status.HTTP_201_CREATED)
        return Response("Input invalido", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def hamburguesa_detail(request, pk):
    try:
        hamburguesa = Hamburguesa.objects.get(pk=pk)
    except Hamburguesa.DoesNotExist:
        return Response("Hamburguesa inexistente",
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HamburguesaSerializer(hamburguesa)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        hamburguesa.delete()
        return Response("Hamburguesa eliminada", status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def ingrediente_list(request):

    if request.method == 'GET':
        snippets = Ingrediente.objects.all()
        serializer = IngredienteSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Ingrediente creado", status=status.HTTP_201_CREATED)
        return Response("Input invalido", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def ingrediente_detail(request, pk):
    try:
        ingrediente = Ingrediente.objects.get(pk=pk)
    except Ingrediente.DoesNotExist:
        return Response("Ingrediente inexistente",
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        ingrediente.delete()
        return Response("Ingrediente eliminado", status=status.HTTP_200_OK)


