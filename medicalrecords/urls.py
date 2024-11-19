from django.urls import path
from .views import create_medical_record,view_medical_record,medical_records_list

urlpatterns = [
    path('',medical_records_list,name="all_records"),
    path('<int:appointment_id>/medical-record/create/', create_medical_record, name='create_medical_record'),
    path('medical-record/<int:appointment_id>/', view_medical_record, name='view_medical_record'),
]