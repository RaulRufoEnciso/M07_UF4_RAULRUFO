from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    tel = models.CharField(max_length=30)
    opcionesDeSexo = (
        ('F', 'Female'),
        ('M', 'Man'),
    )
    sexo = models.CharField(max_length=1, choices=opcionesDeSexo)
