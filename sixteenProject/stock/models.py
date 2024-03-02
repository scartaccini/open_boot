from django.db import models

class Product(models.Model):
    name=models.CharField(blank=False, null=False, max_length=20)
    short_description=models.CharField(blank=False, null=False, max_length=40)
    description=models.TextField(blank=False, null=False, max_length=120)
    quantity=models.IntegerField(default=10)

    def __str__(self):
        return "{} / {} / {} / {}".format(self.name, self.short_description, self.description,self.quantity)