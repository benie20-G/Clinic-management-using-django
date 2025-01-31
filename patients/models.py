from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255,default='Kigali')
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
