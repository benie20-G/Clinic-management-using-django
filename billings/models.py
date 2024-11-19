from django.db import models
from appointments.models import Appointment

class Billing(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Billing for {self.appointment.patient}'
