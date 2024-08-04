from django.contrib import admin
#
from .models import User, Perfil
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'full_name',
        'address',
        'date_birth',
        'gender',
        'codigo',
        'is_active',
        'is_staff',
        'is_superuser',
    )


admin.site.register(User, UserAdmin)


class PerfilAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'user',
        'avatar',
        'type',
    )


admin.site.register(Perfil, PerfilAdmin)