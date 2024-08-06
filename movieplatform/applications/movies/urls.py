from django.urls import path
#
from . import views

app_name = 'category_app'

urlpatterns = [
    path('api/add/category/', views.AddCategory.as_view(), name='add_category'),
    path('api/list/category/', views.ListCategory.as_view(), name='list_category'),
    #
    path('api/add/movie/', views.AddMovie.as_view(), name='add_movie'),
    path('api/list/movie/', views.ListMovies.as_view(), name='listmovie'),
    #
    path('api/add/continuar-viendo/', views.ContianuarViendo.as_view(), name='continuar_viendo'),
    #
    path('api/list/movies-perfil/<pk>/', views.MoviePerfilUser.as_view(), name='list_movie_perfil'),
]