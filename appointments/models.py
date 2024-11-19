from django.db import models
from patients.models import Patient
from doctor.models import Doctor


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    symptoms = models.TextField()

    def __str__(self):
        return f'{self.patient} - {self.appointment_date}'

