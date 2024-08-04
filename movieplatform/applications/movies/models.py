from django.db import models
#
from model_utils.models import TimeStampedModel
#
from applications.users.models import User
#
from django.conf import settings
# Create your models here.

class Category(TimeStampedModel):
    name = models.CharField('Nombre Categoria', max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        unique_together = ('name',)
        ordering = ('id'),        

    def __str__(self):
        return str(self.id)



class Movie(TimeStampedModel):
    name = models.CharField('Nombre Pelicula', max_length=100)
    image = models.ImageField('Imagen', upload_to='movies', blank=True, null=True)
    description = models.TextField('Descripcion', blank=True)
    trailer = models.URLField('Trailer Pelicula', max_length=200, blank=True)
    category = models.ForeignKey(Category, related_name='movie_category', on_delete=models.CASCADE) #relaciona la categoria con la pelicula
    active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'
        unique_together = ('name', 'category',)
    

    def __str__(self):
        return self.name


class ContinuarViendo(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pelicula Usuario'
        verbose_name_plural = 'Peliculas Usuarios'
    

    def __str__(self):
        return f'{self.user.full_name} - {self.movie.name}'
