from django.db import models

class Ruta(models.Model):
    codigo = models.CharField(max_length=6)
    nombre = models.CharField(max_length=30)
    inicio = models.CharField(max_length=30)
    punto1 = models.CharField(max_length=30)
    punto2 = models.CharField(max_length=30)
    punto3 = models.CharField(max_length=30)
    punto4 = models.CharField(max_length=30)
    punto5 = models.CharField(max_length=30)
    fin = models.CharField(max_length=30)
    rutas = models.Manager()

    def __str__(self):
        return "{}".format(self.nombre)
   