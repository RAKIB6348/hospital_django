from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('appointment/', views.appointment_list, name='appointment_list'),
    path('appointment/add/', views.appointment_form, name='appointment_form'),
    path('appointment/edit/<int:appointment_id>/', views.appointment_edit, name='appointment_edit'),
    path('appointment/delete/<int:appointment_id>/', views.appointment_delete, name='appointment_delete'),
    path('department/', views.department, name='department'),
]
