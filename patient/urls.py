from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('appointment/', views.appointment_form, name='appointment_form'),
    path('department/', views.department, name='department'),
]
