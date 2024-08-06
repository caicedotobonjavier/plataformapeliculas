# Generated by Django 5.0.7 on 2024-08-05 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_perfil_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Usuario activo'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Pertenece al Staff'),
        ),
    ]
