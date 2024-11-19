# templatetags/medical_filters.py
from django import template
from medicalrecords.models import MedicalRecord

register = template.Library()

@register.filter
def medicalrecord_exists(appointment_id):
    return MedicalRecord.objects.filter(appointment_id=appointment_id).first()
