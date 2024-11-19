from django import template
from medicalrecords.models import MedicalRecord

register = template.Library()

@register.simple_tag
def has_medical_record(appointment):
    return MedicalRecord.objects.filter(appointment=appointment).exists()
