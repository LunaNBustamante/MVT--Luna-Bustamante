from django.db import models
from datetime import datetime

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    #Agregamos fecha de nacimiento 
    fecha_nac = models.DateFields()

