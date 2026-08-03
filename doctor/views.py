from django.shortcuts import redirect, render
from .models import Doctor


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor/doctor_list.html', {'doctors': doctors})


def doctor_add(request):
    if request.method == 'POST':
        Doctor.objects.create(
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
            available=request.POST.get('available') == 'on',
        )
        return redirect('doctor:doctor_list')
    return render(request, 'doctor/doctor_add.html')
