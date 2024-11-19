from django.shortcuts import render,redirect,get_object_or_404
from .forms import DoctorForm
from .models import Doctor
from django.contrib import messages
from django.db.models import Q



def register_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors_list')
    else:
        form = DoctorForm()
    return render(request,'doctors/create_doctor.html',{'form':form})

# def doctors_list(request):
#     doctors = Doctor.objects.all()
#     return render(request, 'doctors/doctors_list.html', {'doctors': doctors})

def doctors_list(request):
    query = request.GET.get('q', '')  # Get the search query from the GET parameters
    sort_by = request.GET.get('sort', 'name')  # Default sorting by name

    doctors = Doctor.objects.all()  # Start with all doctors

    if query:  # If there's a search query, filter the doctors
        doctors = doctors.filter(
            Q(name__icontains=query) |  # Filter by doctor's name
            Q(email__icontains=query)   # Filter by email
        )

    # Ordering the doctors based on the sort_by parameter
    if sort_by in ['name', 'email']:
        doctors = doctors.order_by(sort_by)

    return render(request, 'doctors/doctors_list.html', {'doctors': doctors, 'query': query, 'sort_by': sort_by})

def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)  # Get the doctor by ID or return 404 if not found
    
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()  # Save the edited doctor details
            return redirect('doctors_list')  # Redirect to the homepage (or any other page)
    else:
        form = DoctorForm(instance=doctor)  # Pre-fill the form with the doctor's current details

    return render(request, 'doctors/edit_doctor.html', {'form': form, 'doctor': doctor})

def delete_doctor(request, doctor_id):
    deldoctor = get_object_or_404(Doctor, id=doctor_id)  # Get the doctor by ID or return 404 if not found

    if request.method == 'POST':
        deldoctor.delete()  # Delete the doctor
        messages.success(request, 'doctor deleted successfully.')  # Add a success message
        return redirect('doctors_list')  # Redirect to the homepage (or any other page)

    # Optionally, handle the case for GET request if necessary (e.g., return a 405 error)
    return redirect('doctors_list')  