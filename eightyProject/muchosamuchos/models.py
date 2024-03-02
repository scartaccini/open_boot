from django.db import models

class Publication(models.Model):
    title=models.CharField(max_length=120)
  
    def __str__(self):
        return self.title

class Note(models.Model):
    headline=models.CharField(max_length=150)
    publications=models.ManyToManyField(Publication)
    
    def __str__(self):
        #return self.reporter.last_name
        return self.headline

# 1 Publication -> N Note
# 1 Note -> N Publication
