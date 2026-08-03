from django.urls import path
from . import views

app_name = 'auth_user'

urlpatterns = [
    path('list/', views.user_list, name='user_list'),
    path('add/', views.user_add, name='user_add'),
    path('edit/<int:user_id>/', views.user_edit, name='user_edit'),
    path('delete/<int:user_id>/', views.user_delete, name='user_delete'),
]
