from django.shortcuts import get_object_or_404, redirect, render
from .models import User


def user_list(request):
    users = User.objects.all()
    return render(request, 'auth_user/user_list.html', {'users': users})


def user_add(request):
    if request.method == 'POST':
        User.objects.create(
            full_name=request.POST['full_name'],
            username=request.POST['username'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            password=request.POST['password'],
            role=request.POST['role'],
            is_active=request.POST.get('is_active') == 'on',
        )
        return redirect('auth_user:user_list')
    return render(request, 'auth_user/user_add.html')


def user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.full_name = request.POST['full_name']
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        user.role = request.POST['role']
        user.is_active = request.POST.get('is_active') == 'on'
        if request.POST.get('password'):
            user.password = request.POST['password']
        user.save()
        return redirect('auth_user:user_list')
    return render(request, 'auth_user/user_edit.html', {'user': user})


def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('auth_user:user_list')
