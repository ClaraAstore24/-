# Generated by Django 4.1.3 on 2022-12-18 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogALYH', '0002_alter_registrar_contraseña_alter_usuario_contraseña'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partidos', models.CharField(max_length=200)),
            ],
        ),
    ]
