from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('list/', views.doctor_list, name='doctor_list'),
    path('add/', views.doctor_add, name='doctor_add'),
    path('edit/<int:doctor_id>/', views.doctor_edit, name='doctor_edit'),
    path('delete/<int:doctor_id>/', views.doctor_delete, name='doctor_delete'),
]
