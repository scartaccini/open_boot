from django.db import models

class Reporter(models.Model):
    name = models.CharField(max_length=50)
    stories_filed = models.IntegerField()
    
