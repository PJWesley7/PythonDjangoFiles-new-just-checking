from django.db import models

# Create your models here.
class movielist(models.Model):
    movie = models.CharField(max_length=50)
    hero = models.CharField(max_length=50)
    heroine = models.CharField(max_length=50)
    releasedate = models.CharField(max_length=50)
