from django.db import models
"""  iniciar sesión con el correo en lugar del username.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True)
    
USERNAME_FIELD = 'email' 
"""