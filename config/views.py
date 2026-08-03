from django.shortcuts import get_object_or_404, redirect, render
from .models import Bed, Ward


def ward_list(request):
    wards = Ward.objects.all()
    return render(request, 'config/ward_list.html', {'wards': wards})


def ward_add(request):
    if request.method == 'POST':
        Ward.objects.create(
            name=request.POST['name'],
            number_of_beds=request.POST['number_of_beds'],
            available_beds=request.POST['available_beds'],
        )
        return redirect('config:ward_list')
    return render(request, 'config/ward_add.html')


def ward_edit(request, ward_id):
    ward = get_object_or_404(Ward, id=ward_id)
    if request.method == 'POST':
        ward.name = request.POST['name']
        ward.number_of_beds = request.POST['number_of_beds']
        ward.available_beds = request.POST['available_beds']
        ward.save()
        return redirect('config:ward_list')
    return render(request, 'config/ward_edit.html', {'ward': ward})


def ward_delete(request, ward_id):
    ward = get_object_or_404(Ward, id=ward_id)
    ward.delete()
    return redirect('config:ward_list')


def bed_list(request):
    beds = Bed.objects.select_related('ward').all()
    return render(request, 'config/bed_list.html', {'beds': beds})


def bed_add(request):
    if request.method == 'POST':
        Bed.objects.create(
            ward=Ward.objects.get(id=request.POST['ward']),
            bed_number=request.POST['bed_number'],
            status=request.POST['status'],
        )
        return redirect('config:bed_list')
    wards = Ward.objects.all()
    return render(request, 'config/bed_add.html', {'wards': wards})


def bed_edit(request, bed_id):
    bed = get_object_or_404(Bed, id=bed_id)
    if request.method == 'POST':
        bed.ward = Ward.objects.get(id=request.POST['ward'])
        bed.bed_number = request.POST['bed_number']
        bed.status = request.POST['status']
        bed.save()
        return redirect('config:bed_list')
    wards = Ward.objects.all()
    return render(request, 'config/bed_edit.html', {'bed': bed, 'wards': wards})


def bed_delete(request, bed_id):
    bed = get_object_or_404(Bed, id=bed_id)
    bed.delete()
    return redirect('config:bed_list')
