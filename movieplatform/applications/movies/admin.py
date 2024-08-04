from django.contrib import admin
#
from .models import Category, Movie, ContinuarViendo
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

admin.site.register(Category, CategoryAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'image',
        'description',
        'trailer',
        'category',
        'active',
    )


admin.site.register(Movie, MovieAdmin)


class ContinuarViendoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'movie',
    )

admin.site.register(ContinuarViendo, ContinuarViendoAdmin)