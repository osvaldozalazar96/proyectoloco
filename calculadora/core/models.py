from django.db import models

class Usuario(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50)
    gmail = models.EmailField()
    password = models.CharField(max_length=50)
def __str__(self):
        return self.usuario
