from django.db import models
from django.contrib.auth.models import User

"""class Artista(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.email)"""

class Grafiti(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=False)
    direccion = models.CharField(max_length=200, blank=False, null=False)
    imagen=models.ImageField(upload_to='fotos', blank=False, null=False)
    #artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return "{}--{}--{}".format(self.name, self.direccion, self.user)
