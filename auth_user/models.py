from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=30, choices=[
        ('admin', 'Admin'),
        ('receptionist', 'Receptionist'),
        ('nurse', 'Nurse'),
        ('doctor', 'Doctor'),
    ], default='receptionist')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
