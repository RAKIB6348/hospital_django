from django.shortcuts import get_object_or_404, redirect, render
from .models import Doctor


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor/doctor_list.html', {'doctors': doctors})


def doctor_add(request):
    if request.method == 'POST':
        Doctor.objects.create(
            image=request.FILES.get('image'),
            name=request.POST['name'],
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
        doctor.name = request.POST['name']
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
