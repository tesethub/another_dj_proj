from django.db import models

# Create your models here.

class Viewed(models.Model):
    ip=models.GenericIPAddressField()
    material=models.CharField(max_length=100)
