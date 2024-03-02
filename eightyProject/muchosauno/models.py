from django.db import models

class Reporter(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Article(models.Model):
    headline=models.CharField(max_length=150)
    publish=models.DateField()
    reporter=models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        #return self.reporter.last_name
        return self.headline

# 1 Reporter -> N Article
# 1 Article -> 1 Reporter
