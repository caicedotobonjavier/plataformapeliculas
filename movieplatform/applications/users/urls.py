from django.urls import path
#
from . import views

app_name = 'users_app'

urlpatterns = [
    path('api/add/user/', views.AddUser.as_view(), name='add_user'),
    path('api/activate/user/<pk>/', views.ActivateUser.as_view(), name='activate_user'),
]
