from django.db import models


# make models here

class Haiku(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
