from django.db import models

class Registro(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    imagen=models.ImageField(upload_to='imagenes', blank=True, null=True)
