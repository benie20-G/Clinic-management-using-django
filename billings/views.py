from django.shortcuts import render, redirect,get_object_or_404
from .models import Billing
from .forms import BillingForm
from appointments.models import Appointment
from django.db.models import Q




def billing_list(request):
    query = request.GET.get('q', '')  # Get the search query from the GET parameters
    sort_by = request.GET.get('sort', 'appointment__doctor__name')  # Default sorting by doctor's name

    # Start with all billing and select related objects for optimization
    bills = Billing.objects.select_related('appointment__doctor', 'appointment__patient').all()

    if query:  # If there's a search query, filter the billing
        bills = bills.filter(
            Q(appointment__doctor__name__icontains=query) |  # Filter by doctor's name
            Q(appointment__patient__name__icontains=query) |  # Filter by patient's name
            Q(appointment__appointment_date__icontains=query) |  # Filter by appointment date
            Q(total_amount__icontains=query)  # Filter by total amount (if needed)
        )

    # Ordering the billing based on the sort_by parameter
    if sort_by in ['appointment__doctor__name', 'appointment__patient__name', 'total_amount', 'is_paid']:
        bills = bills.order_by(sort_by)

    return render(request, 'billings/billing_list.html', {'bills': bills, 'query': query, 'sort_by': sort_by})
    

def create_billing(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            # Save form without committing to the database yet
            billing = form.save(commit=False)
            
            # Get the doctor and patient from the POST data
            appointment= Appointment.objects.get(id=request.POST['appointment'])
            
          
            billing.appointment = appointment
            
            # Now save the billing to the database
            billing.save()
            return redirect('billing_list')
    else:
        form = BillingForm()
        
        
    appointments = Appointment.objects.all()
    return render(request, 'billings/create_billing.html', {
        'form': form,
        'appointments': appointments,
    })

def edit_billing(request, pk):
    bill = get_object_or_404(Billing, pk=pk)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('billing_list')
    else:
        form = BillingForm(instance=bill)
    return render(request, 'billings/edit_billing.html', {'form': form})

def delete_billing(request, pk):
    bill = get_object_or_404(Billing, pk=pk)
    if request.method == 'POST':
        bill.delete()
        return redirect('billing_list')
    return render(request, 'billings/delete_billing.html', {'bill': bill})

