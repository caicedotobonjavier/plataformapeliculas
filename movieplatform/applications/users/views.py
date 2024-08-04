from django.shortcuts import render
#
from .models import User, Perfil
#
from django.http.response import HttpResponseRedirect
#
from django.urls import reverse_lazy, reverse
#
from django.contrib.auth import authenticate, login, logout
#
from .serializers import UserSerializer, ActivateUserSerializer, UserListSerializer, LoginSerializer, PerfilSerializer
#
from rest_framework.views import APIView
#
from rest_framework.response import Response
#
from rest_framework.authtoken.models import Token
#
from rest_framework.authentication import TokenAuthentication
#
from rest_framework.permissions import IsAuthenticated, IsAdminUser
#
from .functions import code_generator, send_mail_google
#

# Create your views here.


# La clase `AddUser` es una vista API en Python que maneja la creación de usuarios validando los datos de entrada.
# generar un código, crear una nueva instancia de usuario, configurar la contraseña, enviar un correo electrónico de activación,
# y redireccionando para activar al usuario.
class AddUser(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        generar_codigo = code_generator()

        user = User.objects.create_user(
            serializer.validated_data['email'],
            full_name = serializer.validated_data['full_name'],
            address = serializer.validated_data['address'],
            date_birth = serializer.validated_data['date_birth'],
            gender = serializer.validated_data['gender'],
            codigo = generar_codigo
        )
        user.set_password(serializer.validated_data['password'])
        user.save()

        if user:
            send_mail_google(codigo=user.codigo, nombre=user.full_name, email=serializer.validated_data['email'])
        

        #este return para trabajar en el navegador
        #return HttpResponseRedirect(
        #    reverse(
        #        'users_app:activate_user',
        #        kwargs={'pk': user.id}
        #    )
        #)

        return Response(
            {
                "mensaje" : "Usuario creado correctamente",
                "url" : f"esta es la url de activacion http://127.0.0.1:8000/api/activate/user/{user.id}/",
                "codigo_activacion" : generar_codigo,
                "ejecucion" : "en postman tome la url con el metodo POST y en el raw pase lo siguiente {'codigo' : 'codigo_activacion'}"
            }
        )
        


# La clase `ActivateUser` es una vista API de Django que activa una cuenta de usuario según una configuración proporcionada.
# código de activación.
class ActivateUser(APIView):
    serializer_class = ActivateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'id_user': self.kwargs['pk']})
        serializer.is_valid(raise_exception=True)

        usuario = User.objects.get(id=self.kwargs['pk'])

        if usuario.codigo == serializer.validated_data['codigo']:
            usuario.is_active = True
            usuario.save()
        
        return Response(
            {
                'Mensaje' : 'Usuario activado correctamente'
            }
        )



class ListUser(APIView):
    serializer_class = UserListSerializer

    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = self.serializer_class(queryset, many=True).data

        return Response(
            serializer
        )



class LoginUser(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(email=usuario, password=password)

        token, created = Token.objects.get_or_create(user=user)

        if user:

            return Response(
                {
                    "mensaje" : f"Bienvenido al sistema: {user.full_name}",
                    "user_name" : user.email,
                    "codigo_verificacion" : user.codigo,
                    "genero" : user.get_gender_display(),
                    "token" : token.key
                }
            )


class AddPerfilUsers(APIView):
    serializer_class = PerfilSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        nombre = serializer.validated_data['name']
        tipo = serializer.validated_data['type']
        usuario = self.request.user

        new_perfil = Perfil.objects.create(
            name = nombre,
            user = usuario,
            type = tipo
        )


        return Response(
            {
                'usuario' : usuario.full_name,
                'nuevo_perfil' : new_perfil.name
            }
        )