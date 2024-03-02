from django.db import models
from datetime import date

class Tarea(models.Model):
    titulo=models.CharField(blank=False, null=False, max_length=100, unique=True)
    descripcion=models.TextField(blank=True, null=True, max_length=200)
    fecha=models.DateField(default=date.today)
    fecha_estimada=models.DateField(blank=True, null=True)
    prioridad=models.IntegerField(default=3)
        
    def __str__(self):
        return "(TAREA): {} _ {} _ {} _ {} _ {} ".format(self.titulo, self.descripcion, self.fecha, self.fecha_estimada, self.prioridad)