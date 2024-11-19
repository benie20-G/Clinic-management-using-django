from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    contact_number = models.CharField(max_length=100,unique=True,default = "0000")

    def __str__(self):
        return self.name