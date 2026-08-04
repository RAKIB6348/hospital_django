from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import Doctor, DoctorSchedule


def doctor_list(request):
    doctors = Doctor.objects.all()
    q = request.GET.get('q', '').strip()
    if q:
        query = Q(first_name__icontains=q) | Q(last_name__icontains=q)
        parts = q.split()
        if len(parts) >= 2:
            query |= Q(first_name__icontains=parts[0], last_name__icontains=' '.join(parts[1:]))
        doctors = doctors.filter(query)
    return render(request, 'doctor/doctor_list.html', {'doctors': doctors, 'q': q})


def doctor_add(request):
    if request.method == 'POST':
        Doctor.objects.create(
            image=request.FILES.get('image'),
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            gender=request.POST['gender'],
            specialization=request.POST['specialization'],
            department=request.POST['department'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            present_address=request.POST['present_address'],
            permanent_address=request.POST['permanent_address'],
            education=request.POST['education'],
            experience_years=request.POST['experience_years'],
            fee=request.POST['fee'],
            wage=request.POST['wage'],
            allowance=request.POST['allowance'],
            contract_start=request.POST.get('contract_start') or None,
            contract_end=request.POST.get('contract_end') or None,
            joining_date=request.POST.get('joining_date') or None,
            available=request.POST.get('available') == 'on',
        )
        return redirect('doctor:doctor_list')
    return render(request, 'doctor/doctor_add.html')


def doctor_edit(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        if request.FILES.get('image'):
            doctor.image = request.FILES['image']
        doctor.first_name = request.POST['first_name']
        doctor.last_name = request.POST['last_name']
        doctor.gender = request.POST['gender']
        doctor.specialization = request.POST['specialization']
        doctor.department = request.POST['department']
        doctor.phone = request.POST['phone']
        doctor.email = request.POST['email']
        doctor.present_address = request.POST['present_address']
        doctor.permanent_address = request.POST['permanent_address']
        doctor.education = request.POST['education']
        doctor.experience_years = request.POST['experience_years']
        doctor.fee = request.POST['fee']
        doctor.wage = request.POST['wage']
        doctor.allowance = request.POST['allowance']
        doctor.contract_start = request.POST.get('contract_start') or None
        doctor.contract_end = request.POST.get('contract_end') or None
        doctor.joining_date = request.POST.get('joining_date') or None
        doctor.available = request.POST.get('available') == 'on'
        doctor.save()
        return redirect('doctor:doctor_list')
    return render(request, 'doctor/doctor_edit.html', {'doctor': doctor})


def doctor_delete(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    doctor.delete()
    return redirect('doctor:doctor_list')


def schedule_list(request):
    schedules = DoctorSchedule.objects.select_related('doctor').all()
    return render(request, 'doctor/schedule_list.html', {'schedules': schedules})


def schedule_add(request):
    if request.method == 'POST':
        DoctorSchedule.objects.create(
            doctor=Doctor.objects.get(id=request.POST['doctor']),
            day_of_week=request.POST['day_of_week'],
            start_time=request.POST['start_time'],
            end_time=request.POST['end_time'],
            available=request.POST.get('available') == 'on',
        )
        return redirect('doctor:schedule_list')
    doctors = Doctor.objects.all()
    return render(request, 'doctor/schedule_add.html', {'doctors': doctors})


def schedule_edit(request, schedule_id):
    schedule = get_object_or_404(DoctorSchedule, id=schedule_id)
    if request.method == 'POST':
        schedule.doctor = Doctor.objects.get(id=request.POST['doctor'])
        schedule.day_of_week = request.POST['day_of_week']
        schedule.start_time = request.POST['start_time']
        schedule.end_time = request.POST['end_time']
        schedule.available = request.POST.get('available') == 'on'
        schedule.save()
        return redirect('doctor:schedule_list')
    doctors = Doctor.objects.all()
    return render(request, 'doctor/schedule_edit.html', {'schedule': schedule, 'doctors': doctors})


def schedule_delete(request, schedule_id):
    schedule = get_object_or_404(DoctorSchedule, id=schedule_id)
    schedule.delete()
    return redirect('doctor:schedule_list')
