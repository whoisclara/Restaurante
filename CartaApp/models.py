from django.db import models

# Create your models here.
class Product(models.Model):
    nombre = models.CharField(max_length=200,default="")
    descripcion = models.CharField(max_length=400, default="")
    img = models.URLField()
