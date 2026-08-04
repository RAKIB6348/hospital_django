from django.shortcuts import get_object_or_404, redirect, render
from .models import Department


def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department/department_list.html', {'departments': departments})


def department_add(request):
    if request.method == 'POST':
        Department.objects.create(
            name=request.POST['name'],
            number_of_doctors=request.POST['number_of_doctors'],
        )
        return redirect('department:department_list')
    return render(request, 'department/department_add.html')


def department_edit(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if request.method == 'POST':
        department.name = request.POST['name']
        department.number_of_doctors = request.POST['number_of_doctors']
        department.save()
        return redirect('department:department_list')
    return render(request, 'department/department_edit.html', {'department': department})


def department_delete(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    department.delete()
    return redirect('department:department_list')
