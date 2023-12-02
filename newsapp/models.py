from django.db import models


# Create your models here.
class Kurs(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    time = models.DateTimeField()

