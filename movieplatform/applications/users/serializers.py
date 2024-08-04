import datetime
#
from .models import User, Perfil
#
from django.contrib.auth import authenticate
#
from rest_framework import serializers
#


# La clase `UserSerializer` define campos para datos de usuario e incluye validación para garantizar la contraseña
# y confirme la coincidencia de contraseña.
class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    full_name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=50)
    date_birth = serializers.DateField()
    gender = serializers.CharField(max_length=1)

    password = serializers.CharField()
    confirm_password = serializers.CharField()


    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        
        return data


# La clase `ActivateUserSerializer` en Python valida un código dado contra el código de un usuario en el
# base de datos.
class ActivateUserSerializer(serializers.Serializer):
    codigo = serializers.CharField()

    def validate(self, data):
        id_user = self.context.get('id_user')

        usuario = User.objects.get(id=id_user)
        print(usuario)

        if usuario.codigo != data['codigo']:
            raise serializers.ValidationError("Codigo incorrecto")
        
        return data



class UserListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    full_name = serializers.CharField()
    address = serializers.CharField()
    date_birth = serializers.DateField()
    gender = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if not authenticate(email=data['email'], password=data['password']):
            raise serializers.ValidationError("Credenciales incorrectas")
        
        return data



class PerfilSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    type = serializers.CharField(max_length=1)