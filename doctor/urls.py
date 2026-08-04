from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('list/', views.doctor_list, name='doctor_list'),
    path('add/', views.doctor_add, name='doctor_add'),
    path('edit/<int:doctor_id>/', views.doctor_edit, name='doctor_edit'),
    path('delete/<int:doctor_id>/', views.doctor_delete, name='doctor_delete'),
    path('schedule/list/', views.schedule_list, name='schedule_list'),
    path('schedule/add/', views.schedule_add, name='schedule_add'),
    path('schedule/edit/<int:schedule_id>/', views.schedule_edit, name='schedule_edit'),
    path('schedule/delete/<int:schedule_id>/', views.schedule_delete, name='schedule_delete'),
]
