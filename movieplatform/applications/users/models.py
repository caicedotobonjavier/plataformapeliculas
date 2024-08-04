from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager
#
from model_utils.models import TimeStampedModel
#
from django.conf import settings
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    MASCULINO = '0'
    FEMENINO = '1'
    OTRO = '2'

    CHOICES_GENDER = (
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        (OTRO, 'Otro'),
    )
    

    email = models.EmailField('Correo Electronico', max_length=254, unique=True)
    full_name = models.CharField('Nombre Completo', max_length=100)
    address = models.CharField('Direccion Domicilio', max_length=50, blank=True)
    date_birth = models.DateField('Fecha de Nacimiento', blank=True, null=True)
    gender = models.CharField('Genero', max_length=1, choices=CHOICES_GENDER, blank=True)
    codigo = models.CharField('Codigo', max_length=6, blank=True)

    is_active = models.BooleanField('Usuario activo', default=False)
    is_staff = models.BooleanField('Pertenece al Staff', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    

    def get_email(self):
        return self.email
    
    def get_full_name(self):
        return self.full_name


class Perfil(TimeStampedModel):
    INFANTIL = '0'
    ADULTOS = '1'
    OTRO = '2'

    TIPO_PERFIL = (
        (INFANTIL, 'Infantil'),
        (ADULTOS, 'Adultos'),
        (OTRO, 'Otro'),
    )
    
    name = models.CharField('Nombre Perfil', max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='perfil_user', on_delete=models.CASCADE)
    avatar = models.ImageField('Imagen de Perfil', upload_to='perfil', blank=True, null=True)
    type = models.CharField('Tipo de Perfil', max_length=1, choices=TIPO_PERFIL)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    

    def __str__(self):
        return self.name