from django.db import models

class Employee(models.Model):
    name=models.CharField(blank=False, null=False, max_length=20)
    last_name=models.CharField(blank=False, null=False, max_length=40)
    email=models.EmailField(blank=False, null=False, max_length=60)

    def __str__(self):
        return "{} / {} / {}".format(self.name, self.last_name, self.email)