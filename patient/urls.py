from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('appointment/', views.appointment_list, name='appointment_list'),
    path('appointment/add/', views.appointment_form, name='appointment_form'),
    path('appointment/edit/<int:appointment_id>/', views.appointment_edit, name='appointment_edit'),
    path('appointment/delete/<int:appointment_id>/', views.appointment_delete, name='appointment_delete'),
    path('api/doctors-by-department/', views.doctors_by_department, name='doctors_by_department'),
    path('appointment/doctor-info/<int:doctor_id>/', views.doctor_info, name='doctor_info'),
    path('department/', views.department, name='department'),
]
