from django.shortcuts import redirect, render
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
    return render(request, 'department/department_add.html')
