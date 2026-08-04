import datetime

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Appointment
from config.models import Bed, Ward
from department.models import Department
from doctor.models import Doctor, DoctorSchedule

DAY_INDEX = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6,
}


def schedule_label(schedule):
    start = schedule.start_time.strftime('%I:%M %p').lstrip('0')
    end = schedule.end_time.strftime('%I:%M %p').lstrip('0')
    return f"{schedule.get_day_of_week_display()} — {start} to {end}"


def validate_schedule(schedule, department_id, doctor_id, date, exclude_id=None):
    if schedule is None:
        return False, 'Please choose a schedule.'
    if not schedule.available:
        return False, f'The selected schedule "{schedule_label(schedule)}" is currently unavailable.'
    if schedule.doctor_id != doctor_id:
        return False, 'The selected schedule does not belong to the chosen doctor.'
    if schedule.doctor.department_id != department_id:
        return False, 'The chosen doctor does not belong to the selected department.'
    weekday = date.weekday()
    if DAY_INDEX.get(schedule.day_of_week) != weekday:
        return False, (
            f'The selected date is on {date:%A}, but this schedule is for '
            f'{schedule.get_day_of_week_display()}.'
        )
    booked = Appointment.objects.filter(schedule=schedule, date=date)
    if exclude_id:
        booked = booked.exclude(id=exclude_id)
    if booked.exists():
        return False, (
            f'This time slot ({schedule_label(schedule)}) is already booked '
            f'on {date:%d %b %Y}. Please choose another.'
        )
    return True, ''


def resolve_selected(appointment):
    if appointment.schedule_id:
        schedule = appointment.schedule
        return schedule.doctor.department_id, schedule.doctor_id
    department = Department.objects.filter(name=appointment.department).first()
    doctors = Doctor.objects.filter(
        Q(first_name__icontains=appointment.doctor)
        | Q(last_name__icontains=appointment.doctor)
    )
    if department is not None:
        doctors = doctors.filter(department=department)
    doctor = doctors.first()
    return department.id if department else None, doctor.id if doctor else None


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
    q = request.GET.get('q', '').strip()
    if q:
        appointments = appointments.filter(
            Q(patient_name__icontains=q)
            | Q(phone__icontains=q)
            | Q(department__icontains=q)
            | Q(doctor__icontains=q)
            | Q(reason__icontains=q)
        )
    return render(request, 'patient/appointment_list.html', {
        'appointments': appointments,
        'q': q,
    })


def appointment_form(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        department = Department.objects.filter(id=request.POST['department']).first()
        doctor = Doctor.objects.filter(id=request.POST['doctor']).first()
        schedule = DoctorSchedule.objects.filter(id=request.POST['schedule']).first()
        date = datetime.date.fromisoformat(request.POST['date'])

        valid, error = validate_schedule(
            schedule,
            int(request.POST['department']),
            int(request.POST['doctor']),
            date,
        )
        if not valid:
            return render(request, 'patient/appointment_form.html', {
                'departments': departments,
                'error': error,
                'selected_department_id': int(request.POST['department']),
                'selected_doctor_id': int(request.POST['doctor']),
                'selected_schedule_id': int(request.POST['schedule']),
                'form_data': {
                    'patient_name': request.POST['patient_name'],
                    'patient_age': request.POST['patient_age'],
                    'gender': request.POST['gender'],
                    'address': request.POST['address'],
                    'date': request.POST['date'],
                    'phone': request.POST['phone'],
                    'reason': request.POST['reason'],
                },
            })

        Appointment.objects.create(
            patient_name=request.POST['patient_name'],
            patient_age=request.POST['patient_age'],
            gender=request.POST['gender'],
            address=request.POST['address'],
            department=department.name,
            doctor=doctor.full_name,
            schedule=schedule,
            consultation_fee=doctor.fee,
            date=date,
            time=schedule.start_time,
            phone=request.POST['phone'],
            reason=request.POST['reason'],
        )
        return redirect('appointment_list')
    return render(request, 'patient/appointment_form.html', {
        'departments': departments,
    })


def appointment_edit(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    departments = Department.objects.all()
    if request.method == 'POST':
        department = Department.objects.filter(id=request.POST['department']).first()
        doctor = Doctor.objects.filter(id=request.POST['doctor']).first()
        schedule = DoctorSchedule.objects.filter(id=request.POST['schedule']).first()
        date = datetime.date.fromisoformat(request.POST['date'])

        valid, error = validate_schedule(
            schedule,
            int(request.POST['department']),
            int(request.POST['doctor']),
            date,
            exclude_id=appointment.id,
        )
        if not valid:
            return render(request, 'patient/appointment_edit.html', {
                'appointment': appointment,
                'departments': departments,
                'error': error,
                'selected_department_id': int(request.POST['department']),
                'selected_doctor_id': int(request.POST['doctor']),
                'selected_schedule_id': int(request.POST['schedule']),
                'form_data': {
                    'patient_name': request.POST['patient_name'],
                    'patient_age': request.POST['patient_age'],
                    'gender': request.POST['gender'],
                    'address': request.POST['address'],
                    'date': request.POST['date'],
                    'phone': request.POST['phone'],
                    'reason': request.POST['reason'],
                },
            })

        appointment.patient_name = request.POST['patient_name']
        appointment.patient_age = request.POST['patient_age']
        appointment.gender = request.POST['gender']
        appointment.address = request.POST['address']
        appointment.department = department.name
        appointment.doctor = doctor.full_name
        appointment.schedule = schedule
        appointment.consultation_fee = doctor.fee
        appointment.date = date
        appointment.time = schedule.start_time
        appointment.phone = request.POST['phone']
        appointment.reason = request.POST['reason']
        appointment.save()
        return redirect('appointment_list')

    department_id, doctor_id = resolve_selected(appointment)
    return render(request, 'patient/appointment_edit.html', {
        'appointment': appointment,
        'departments': departments,
        'selected_department_id': department_id,
        'selected_doctor_id': doctor_id,
        'selected_schedule_id': appointment.schedule_id,
    })


def appointment_delete(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.delete()
    return redirect('appointment_list')


def doctors_by_department(request):
    department_id = request.GET.get('department_id')
    if not department_id:
        return JsonResponse({'doctors': []})
    doctors = Doctor.objects.filter(
        department_id=department_id,
        available=True,
    ).order_by('first_name', 'last_name')
    return JsonResponse({'doctors': [
        {'id': d.id, 'name': d.full_name} for d in doctors
    ]})


def doctor_info(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    schedules = DoctorSchedule.objects.filter(doctor=doctor, available=True)
    return JsonResponse({
        'consultation_fee': f'{doctor.fee:.2f}',
        'schedules': [
            {'id': s.id, 'label': schedule_label(s)} for s in schedules
        ],
    })


def department(request):
    return render(request, 'patient/department.html')
