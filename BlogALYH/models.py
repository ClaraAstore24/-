from django.db import models

# Create your models here.

class Usuario(models.Model):
    contraseña = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f" Email: {self.email} / Contraseña: {self.contraseña}"


class Registrar(models.Model):
    nombre = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f" Nombre: {self.nombre.upper()} / Email: {self.email} / Contraseña: {self.contraseña} "

class Publicaciones(models.Model):
    comentarios = models.CharField(max_length=280)
    
    def __str__(self):
        return f"Comentarios: {self.comentarios}"



