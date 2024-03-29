from django.db import models

from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    imagen=models.ImageField(upload_to='img_servicios', blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    
       

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
