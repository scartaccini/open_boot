from django.db import models
from datetime import date

class Agenda(models.Model):
    nombre=models.CharField(blank=False, null=False, max_length=20)
    apellido=models.CharField(blank=False, null=False, max_length=40)
    tel=models.CharField(blank=True, null=True, max_length=12)
    cel=models.CharField(blank=False, null=False, max_length=12, unique=True)
    email=models.EmailField(unique=True, blank=False, null=False)
    compania=models.CharField(blank=True, null=True, max_length=50)
    fecha=models.DateField(default=date.today)
    notas=models.TextField(blank=True, null=True, max_length=150)
    
    def __str__(self):
        return "(AGENDA): {} _ {} _ {} _ {} _ {} _ {} _ {} _ {}".format(self.nombre, self.apellido, self.tel, self.cel, self.email, self.compania, self.fecha, self.notas)
