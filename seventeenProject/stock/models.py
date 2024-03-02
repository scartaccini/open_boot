from django.db import models
from datetime import date

class Product(models.Model):
    name=models.CharField(blank=False, null=False, max_length=20, verbose_name="NOMBRE")
    ##verbose_name="NOMBRE" mantiene en la bd name pero muestra NOMBRE en los formularios y panel
    short_description=models.CharField(blank=False, null=False, max_length=40)
    description=models.TextField(blank=False, null=False, max_length=120)
    quantity=models.IntegerField(default=10)
    fecha=models.DateField(default=date.today)

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.name, self.short_description, self.description,self.quantity, self.fecha)