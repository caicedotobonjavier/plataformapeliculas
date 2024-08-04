from django.shortcuts import render
#
from .models import Category, Movie
#
from .serializers import CategorySerializer, CategoryListSerializer, MovieSerializer, MovieListSerializer
#
from rest_framework.views import APIView
#
from rest_framework.response import Response
# Create your views here.


# La clase `AddCategory` define un método POST para crear una nueva categoría usando datos de un serializador
# y devuelve una respuesta confirmando el registro exitoso de la categoría.
class AddCategory(APIView):
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        name_category = serializer.validated_data['name']

        Category.objects.create(
            name = name_category
        )


        return Response(
            {
                'Mensaje' : f'La categoria - [{name_category}] - se registro correctamente'
            }
        )


# La clase `ListCategory` es una vista API en Python que recupera todas las instancias de `Category`
# modela y los serializa usando `CategoryListSerializer`.
class ListCategory(APIView):
    serializer_class = CategoryListSerializer

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = self.serializer_class(queryset, many=True).data

        return Response(
            serializer
        )



# Esta clase de Python `AddMovie` define un método POST para agregar una película con atributos específicos al
# base de datos.
class AddMovie(APIView):
    serializer_class = MovieSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']
        description = serializer.validated_data['description']
        trailer = serializer.validated_data['trailer']
        categoria = Category.objects.get(id=serializer.validated_data['category'])

        Movie.objects.create(
            name = name,
            description = description,
            trailer = trailer,
            category = categoria
        )


        return Response(
            {
                'Mensaje' : f'La pelicula [{name}] de la categoria [{categoria.name}] se agrego correcamente'
            }
        )



# La clase `ListMovies` es una vista API en Python que recupera todos los objetos de películas de la base de datos.
# y los serializa usando `MovieListSerializer`.
class ListMovies(APIView):
    serializer_class = MovieListSerializer

    def get(self, request, *args, **kwargs):
        queryset = Movie.objects.all()
        serializer = self.serializer_class(queryset, many=True).data

        return Response(
            serializer
        )