from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Hamburguesa
from .models import Ingrediente

from .serializer import IngredienteSerializer, HamburguesaSerializer

def index(request):
    return HttpResponse("Bienvenido a la pagina de hamburguesas, prueba /hamburguesa o /ingrediente")

@api_view(['GET', 'POST'])
def hamburguesa_list(request):

    if request.method == 'GET':
        serializer_context = {
            'request': request,}
        snippets = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(snippets, context=serializer_context, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HamburguesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response("Input invalido", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PATCH'])
def hamburguesa_detail(request, *args, **kwargs):
    pk = kwargs['pk']
    if pk.isnumeric():
        pk = int(pk)
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

        elif request.method == 'PATCH':
            hamburguesa = Hamburguesa.objects.get(pk=pk)
            serializer = HamburguesaSerializer(hamburguesa, data=request.data, partial=True)
            if ('nombre' in serializer.initial_data.keys()) or \
                    ('descripcion' in serializer.initial_data.keys()) or \
                    ('precio' in serializer.initial_data.keys()) or \
                    ('imagen' in serializer.initial_data.keys()):
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("Parametros invalidos", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("id invalido",
                        status=status.HTTP_400_BAD_REQUEST)


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
def ingrediente_detail(request, *args, **kwargs):
    pk = kwargs['pk']
    if pk.isnumeric():
        pk = int(pk)
        try:
            ingrediente = Ingrediente.objects.get(pk=pk)
        except Ingrediente.DoesNotExist:
            return Response("Ingrediente inexistente",
                            status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = IngredienteSerializer(ingrediente)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'DELETE':
            en_hamburguesa = Hamburguesa.objects.filter(ingredientes=ingrediente).count()
            if en_hamburguesa == 0:
                ingrediente.delete()
                return Response("Ingrediente eliminado", status=status.HTTP_200_OK)
            else:
                return Response("Ingrediente no se puede borrar, se encuentra presente en una hamburguesa", status=status.HTTP_409_CONFLICT)
    else:
        return Response("id invalido",
                        status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT', 'DELETE'])
def hamburguesa_ingrediente(request, *args, **kwargs):
    pk = kwargs['pk']
    pk2 = kwargs['pk2']
    if ((pk.isnumeric()) and (pk2.isnumeric())):
        print("ntro")
        try:
            hamburguesa = Hamburguesa.objects.get(pk=pk)
        except Hamburguesa.DoesNotExist:
            return Response("Id de hamburguesa invalido",
                            status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            try:
                ingrediente = Ingrediente.objects.get(pk=pk2)
            except:
                return Response("Ingrediente inexistente",
                                status=status.HTTP_404_NOT_FOUND)
            hamburguesa.ingredientes.add(ingrediente)
            return Response("Ingrediente agregado", status=status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
            try:
                ingrediente = hamburguesa.ingredientes.get(pk=pk2)
            except:
                return Response("Ingrediente inexistente en la hamburguesa",
                                status=status.HTTP_404_NOT_FOUND)
            hamburguesa.ingredientes.remove(ingrediente)
            return Response("Ingrediente retirado", status=status.HTTP_200_OK)
    else:
        return Response("id invalidos, debes ingresar enteros",
                        status=status.HTTP_400_BAD_REQUEST)
    