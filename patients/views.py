
from .models import Patient
from .forms import PatientForm
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from django.db.models import Q

def index(request):
    return render(request, 'patients/index.html')

def patient_list(request):
    query = request.GET.get('q', '')  # Get the search query from the GET parameters
    sort_by = request.GET.get('sort', 'name')  # Default sorting by name

    patients = Patient.objects.all()  # Start with all patients

    if query:  # If there's a search query, filter the patients
        patients = patients.filter(
            Q(name__icontains=query) |  # Filter by patient's name
            Q(email__icontains=query) |  # Filter by email
            Q(contact_number__icontains=query)  # Filter by contact number
        )

    # Ordering the patients based on the sort_by parameter
    if sort_by in ['name', 'email', 'dob', 'contact_number']:
        patients = patients.order_by(sort_by)

    return render(request, 'patients/patient_list.html', {'patients': patients, 'query': query, 'sort_by': sort_by})

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()  # Save the patient data to the database
            return redirect('patient_list')  # Redirect to the homepage after successful form submission
    else:
        form = PatientForm()

    return render(request, 'patients/create_patient.html', {'form': form})

def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)  # Get the patient by ID or return 404 if not found
    
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()  # Save the edited patient details
            return redirect('index')  # Redirect to the homepage (or any other page)
    else:
        form = PatientForm(instance=patient)  # Pre-fill the form with the patient's current details

    return render(request, 'patients/edit_patient.html', {'form': form, 'patient': patient})

def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)  # Get the patient by ID or return 404 if not found

    if request.method == 'POST':
        patient.delete()  # Delete the patient
        messages.success(request, 'Patient deleted successfully.')  # Add a success message
        return redirect('patient_list')  # Redirect to the homepage (or any other page)

    # Optionally, handle the case for GET request if necessary (e.g., return a 405 error)
    return redirect('patient_list')  