from django.db import models

class Place(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    numbre_of_employees=models.IntegerField(default=1)
    place=models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.place.address

# 1 Restaurant -> 1 Place 
# 1 Place -> 1 Restaurant