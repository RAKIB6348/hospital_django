from django.shortcuts import get_object_or_404, redirect, render

from .models import Appointment
from config.models import Bed, Ward
from department.models import Department
from doctor.models import Doctor


def dashboard(request):
    context = {
        'total_appointments': Appointment.objects.count(),
        'total_doctors': Doctor.objects.count(),
        'available_doctors': Doctor.objects.filter(available=True).count(),
        'total_departments': Department.objects.count(),
        'total_wards': Ward.objects.count(),
        'total_beds': Bed.objects.count(),
        'available_beds': Bed.objects.filter(status='available').count(),
        'recent_appointments': Appointment.objects.order_by('-date', '-time')[:5],
    }
    return render(request, 'patient/dashboard.html', context)


def appointment_list(request):
    appointments = Appointment.objects.all().order_by('-date', '-time')
    return render(request, 'patient/appointment_list.html', {'appointments': appointments})


def appointment_form(request):
    if request.method == 'POST':
        Appointment.objects.create(
            patient_name=request.POST['patient_name'],
            patient_age=request.POST['patient_age'],
            gender=request.POST['gender'],
            address=request.POST['address'],
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


def appointment_edit(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        appointment.patient_name = request.POST['patient_name']
        appointment.patient_age = request.POST['patient_age']
        appointment.gender = request.POST['gender']
        appointment.address = request.POST['address']
        appointment.department = request.POST['department']
        appointment.doctor = request.POST['doctor']
        appointment.date = request.POST['date']
        appointment.time = request.POST['time']
        appointment.phone = request.POST['phone']
        appointment.reason = request.POST['reason']
        appointment.save()
        return redirect('appointment_list')
    departments = Department.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'patient/appointment_edit.html', {
        'appointment': appointment,
        'departments': departments,
        'doctors': doctors,
    })


def appointment_delete(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.delete()
    return redirect('appointment_list')


def department(request):
    return render(request, 'patient/department.html')
