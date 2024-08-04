from django.shortcuts import render
#
from .models import User, Perfil
#
from django.http.response import HttpResponseRedirect
#
from django.urls import reverse_lazy, reverse
#
from .serializers import UserSerializer, ActivateUserSerializer
#
from rest_framework.views import APIView
#
from rest_framework.response import Response
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
        

        
        return HttpResponseRedirect(
            reverse(
                'users_app:activate_user',
                kwargs={'pk': user.id}
            )
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