from django.shortcuts import render
#
from .models import Category, Movie, ContinuarViendo
#
from applications.users.models import Perfil, User
#
from django.shortcuts import get_object_or_404
#
from .serializers import CategorySerializer, CategoryListSerializer, MovieSerializer, MovieListSerializer, ContinuarViendoSerializer, MoviesTheUserPerfil
#
from rest_framework.views import APIView
#
from rest_framework.response import Response
#
from rest_framework.authentication import TokenAuthentication
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




# Esta clase de Python define una vista para continuar viendo una película, donde crea una nueva entrada en
# la base de datos para el perfil de usuario y la película que se está viendo.
class ContianuarViendo(APIView):
    serializer_class = ContinuarViendoSerializer
    authentication_classes = (TokenAuthentication,)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        perfil_usuario = Perfil.objects.get(id=serializer.validated_data['perfil'])
        pelicula = Movie.objects.get(id=serializer.validated_data['movie'])

        print(perfil_usuario.user.full_name, pelicula.name)

        ContinuarViendo.objects.create(
            perfil = perfil_usuario,
            movie = pelicula
        )        


        return Response(
            {
                'usuario' : f'El usuario: [{perfil_usuario.user.full_name}]',
                'perfil' : f'Con perfil : [{perfil_usuario}]',
                'pelicula' : f'Esta viendo la pelicula: [{pelicula}]'
            }
        )


# Esta clase es una vista API en Python que recupera y serializa datos de películas en el archivo de un usuario.
# perfil.
class MoviePerfilUser(APIView):
    serializer_class = MoviesTheUserPerfil

    
    def get(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        queryset = ContinuarViendo.objects.filter(perfil=id)
        print(queryset)
        serializer = self.serializer_class(queryset, many=True).data
        

        return Response(serializer)