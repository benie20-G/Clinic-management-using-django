from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=128)  #  char field

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.email}"
