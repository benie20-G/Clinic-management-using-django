from django.db import models
from appointments.models import Appointment
# Create your models here.
class MedicalRecord(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment = models.TextField()

    def __str__(self):
        return f'{self.appointment.patient} - {self.diagnosis}'
