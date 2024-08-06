#
from .models import Category, Movie
#
from rest_framework import serializers


# La clase `CategorySerializer` es una clase de Python para serializar datos de categorías con un campo para
# nombre de la categoría.
class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)


# La clase `CategoryListSerializer` es un serializador de Python con campos para identificación y nombre.
class CategoryListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)


# La clase `MovieSerializer` define campos para serializar datos de películas, incluidos nombre, descripción,
# URL del tráiler y categoría.
class MovieSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    trailer = serializers.URLField()
    category = serializers.IntegerField()


# Esta clase define un serializador para una lista de películas con campos para identificación, nombre, imagen, descripción,
# URL del avance, categoría y estado activo.
class MovieListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    image = serializers.ImageField()
    description = serializers.CharField()
    trailer = serializers.URLField()
    category = serializers.CharField()
    active = serializers.BooleanField()


class ContinuarViendoSerializer(serializers.Serializer):
    perfil = serializers.IntegerField()
    movie = serializers.IntegerField()


class MoviesTheUserPerfil(serializers.Serializer):
    id = serializers.IntegerField()
    perfil = serializers.CharField()
    movie = serializers.CharField()