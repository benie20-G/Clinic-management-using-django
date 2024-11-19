from django.shortcuts import render, redirect
from .models import Appointment
from patients.models import Patient
from .forms import AppointmentForm
from doctor.models import Doctor
from django.db.models import Q


from django.shortcuts import render, redirect
from .models import Doctor, Patient
from .forms import AppointmentForm


def appointment_list(request):
    query = request.GET.get('q', '')  # Get the search query from the GET parameters
    appointments = Appointment.objects.all()  # Start with all appointments

    if query:  # If there's a search query, filter the appointments
        appointments = appointments.filter(
            Q(patient__name__icontains=query) |  # Filter by patient's name
            Q(doctor__name__icontains=query) |   # Filter by doctor's name
            Q(appointment_date__icontains=query)  # Filter by appointment date
        )

    return render(request, 'appointments/appointment_list.html', {'appointments': appointments, 'query': query})

def create_appointment(request):
    # Always fetch doctors and patients regardless of the request method
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Save form without committing to the database yet
            appointment = form.save(commit=False)
            
            # Get the doctor and patient from the POST data
            doctor = Doctor.objects.get(id=request.POST['doctor'])
            patient = Patient.objects.get(id=request.POST['patient'])
            
            # Assign the doctor and patient to the appointment
            appointment.doctor = doctor
            appointment.patient = patient
            
            # Now save the appointment to the database
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/create_appointment.html', {
        'form': form,
        'patients': patients,
        'doctors': doctors
    })


def cancel_appointment(request, doctor_id):
    can_appointment = get_object_or_404(Appointment, appointment_id=appointment_id)  # Get the doctor by ID or return 404 if not found

    if request.method == 'POST':
        can_appointment.delete()  # Delete the doctor
        messages.success(request, 'Appointment is canceled successfully.')  # Add a success message
        return redirect('appointment_list')  # Redirect to the homepage (or any other page)

    # Optionally, handle the case for GET request if necessary (e.g., return a 405 error)
    return redirect('appointment_list')  

# def create_appointment(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             # Save form without committing to the database yet
#             appointment = form.save(commit=False)
            
#             # Get the doctor and patient from the POST data
#             doctor = Doctor.objects.get(id=request.POST['doctor'])
#             patient = Patient.objects.get(id=request.POST['patient'])
            
#             # Assign the doctor and patient to the appointment
#             appointment.doctor = doctor
#             appointment.patient = patient
            
#             # Now save the appointment to the database
#             appointment.save()
#             return redirect('appointment_list')
#     else:
        
#         form = AppointmentForm()

#         doctors = Doctor.objects.all()
#         patients = Patient.objects.all()
          
        
#         return render(request, 'appointments/create_appointment.html', {
#             'form': form,
#             'patients': patients,
#             'doctors': doctors
#         })