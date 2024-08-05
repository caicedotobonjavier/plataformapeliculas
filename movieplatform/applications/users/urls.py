from django.urls import path
#
from . import views

app_name = 'users_app'

urlpatterns = [
    path('api/add/user/', views.AddUser.as_view(), name='add_user'),
    path('api/activate/user/<pk>/', views.ActivateUser.as_view(), name='activate_user'),
    #
    path('api/list/user/', views.ListUser.as_view(), name='list_user'),
    #
    path('api/login/user/', views.LoginUser.as_view(), name='login_user'),
    path('api/update-password/user/', views.UpdatePassword.as_view(), name='update_password'),
    #
    path('api/add/perfil/user/', views.AddPerfilUsers.as_view(), name='add_perfil'),
]
