from django.shortcuts import render,get_object_or_404,redirect
from .forms import MedicalRecordForm
from .models import MedicalRecord
from appointments.models import Appointment


def create_medical_record(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            medical_record = form.save(commit=False)
            medical_record.appointment = appointment  # Set the appointment
            medical_record.save()
            return redirect('view_medical_record', pk=appointment_id)  # Redirect to the detail page
    else:
        form = MedicalRecordForm()

    return render(request, 'medical_records/create_medical_record.html', {
        'form': form,
        'appointment': appointment
    })

# def view_medical_records(request, pk):
#     # Fetch the medical records for the specified appointment
#     appointment_id = request.GET.get('appointment_id', None)
#     medical_records = MedicalRecord.objects.all()

#     if appointment_id:
#         medical_records = medical_records.filter(appointment__id=appointment_id)

#     return render(request, 'medical_records/view_records.html', {
#         'medical_records': medical_records,
#         'request': request
#     })


def view_medical_record(request,appointment_id):
    # medical_records = MedicalRecord.objects.all()
    # medical_record = medical_records.filter(appointment_id=appointment_id)
    medical_record = get_object_or_404(MedicalRecord, appointment_id=appointment_id)
    if medical_record:
        return render(request, 'medical_records/view_medical_record.html', {
        'medical_record':medical_record
        })
    else:
        return redirect('appointments_list')

def medical_records_list(request):
    medical_records = MedicalRecord.objects.all()

    return render(request, 'medical_records/view_medical_records.html', {
        'medical_records': medical_records,
    })

    
