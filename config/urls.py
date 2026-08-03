from django.urls import path
from . import views

app_name = 'config'

urlpatterns = [
    path('ward/list/', views.ward_list, name='ward_list'),
    path('ward/add/', views.ward_add, name='ward_add'),
    path('ward/edit/<int:ward_id>/', views.ward_edit, name='ward_edit'),
    path('ward/delete/<int:ward_id>/', views.ward_delete, name='ward_delete'),
    path('bed/list/', views.bed_list, name='bed_list'),
    path('bed/add/', views.bed_add, name='bed_add'),
    path('bed/edit/<int:bed_id>/', views.bed_edit, name='bed_edit'),
    path('bed/delete/<int:bed_id>/', views.bed_delete, name='bed_delete'),
]
