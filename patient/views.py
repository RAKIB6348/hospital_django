from django.shortcuts import redirect, render

from .models import Appointment
from department.models import Department
from doctor.models import Doctor


def dashboard(request):
    return render(request, 'patient/dashboard.html')


def appointment_list(request):
    appointments = Appointment.objects.all().order_by('-date', '-time')
    return render(request, 'patient/appointment_list.html', {'appointments': appointments})


def appointment_form(request):
    if request.method == 'POST':
        Appointment.objects.create(
            patient_name=request.POST['patient_name'],
            patient_age=request.POST['patient_age'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            date=request.POST['date'],
            time=request.POST['time'],
            phone=request.POST['phone'],
            reason=request.POST['reason'],
        )
        return redirect('appointment_list')
    departments = Department.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'patient/appointment_form.html', {
        'departments': departments,
        'doctors': doctors,
    })


def department(request):
    return render(request, 'patient/department.html')
