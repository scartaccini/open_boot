from django.db import models

class Coment(models.Model):
    name=models.CharField(max_length=255, null=False)
    score=models.IntegerField(default=3)
    coment=models.TextField(max_length=1000, null=True)
    date=models.DateField(null=True)
    
    def __str__(self):
        return self.name

#cada vez que se cambie models.py
# python manage.py makemigrations
# python manage.py migrate