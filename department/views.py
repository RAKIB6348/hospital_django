from django.shortcuts import get_object_or_404, redirect, render
from doctor.models import Doctor
from .models import Department


def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department/department_list.html', {'departments': departments})


def department_add(request):
    if request.method == 'POST':
        Department.objects.create(
            name=request.POST['name'],
            head_doctor=request.POST['head_doctor'],
            number_of_doctors=request.POST['number_of_doctors'],
            available_beds=request.POST['available_beds'],
        )
        return redirect('department:department_list')
    doctors = Doctor.objects.all()
    return render(request, 'department/department_add.html', {'doctors': doctors})


def department_edit(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if request.method == 'POST':
        department.name = request.POST['name']
        department.head_doctor = request.POST['head_doctor']
        department.number_of_doctors = request.POST['number_of_doctors']
        department.available_beds = request.POST['available_beds']
        department.save()
        return redirect('department:department_list')
    doctors = Doctor.objects.all()
    return render(request, 'department/department_edit.html', {'department': department, 'doctors': doctors})


def department_delete(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    department.delete()
    return redirect('department:department_list')
