from django.db import models

class Salary(models.Model):
    amount=models.IntegerField(blank=False, null=False, unique=True)
    extra_dec=models.BooleanField(default=False)
    extra_jun=models.BooleanField(default=False)
    
    def __str__(self):
        return "(SALARIO): {} _ {} _ {}".format(self.amount, self.extra_dec, self.extra_jun)

class Country(models.Model):
    name=models.CharField(max_length=50,blank=False, null=False, unique=True)
        
    def __str__(self):
        return "(PAIS): {}".format(self.name)

class Location(models.Model):
    name=models.CharField(max_length=50,blank=False, null=False, unique=True)
    country=models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return "(BARRIO): {} - {}".format(self.name,self.country.name) 
        
class Place(models.Model):
    name=models.CharField(max_length=100,blank=False, null=False, unique=True)
    address=models.CharField(max_length=50, blank=False, null=False, unique=True)
    zip=models.CharField(max_length=5, blank=False, null=False)
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
            
    def __str__(self):
        return "(LUGAR): {}***{}***{}***{}***{}".format(self.name, self.address, self.zip, self.location.name, self.location.country.name)       

class Job(models.Model):
    title=models.CharField(max_length=15, blank=False, null=False, unique=True)
    description=models.TextField(null=True)
    salary=models.ForeignKey(Salary, on_delete=models.CASCADE)

    def __str__(self):
        return "(TRABAJO): {} - {} - {}".format(self.title,self.description,self.salary) 

class Employee(models.Model):
    name=models.CharField(max_length=30, blank=False, null=False)
    last_name=models.CharField(max_length=50, blank=False, null=False)
    email=models.EmailField(max_length=50, blank=False, null=False, unique=True)
    address=models.CharField(max_length=50, blank=False, null=False)
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    place=models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return "(EMPLEADO) : {} {} {} {} {} {}".format(self.name, self.last_name, self.email, self.address, self.job, self.place)

###############
# 1 Employee -> 1 Job       1 Job -> 1 Salary
# 1 Job -> N Employee       1 Salary -> N Job

# 1 Employee -> 1 Place     1 Place -> 1 Location
# 1 Place -> N Employee     1 Location -> N Place

#               1 Location -> 1 Country     
#               1 Country -> N Location

# 1 Empleado -> 1 Trabajo       1 Trabajo -> 1 Salario
# 1 Trabajo -> N Empleado       1 Salario -> N Trabajo

# 1 Emplado -> 1 Lugar     1 Lugar -> 1 Barrio
# 1 Lugar -> N Empleado     1 Barrio -> N Lugar

#               1 Barrio -> 1 Pais     
#               1 Pais -> N Barrio