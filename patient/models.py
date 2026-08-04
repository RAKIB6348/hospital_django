from django.db import models


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], default='male')
    address = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    schedule = models.ForeignKey(
        'doctor.DoctorSchedule',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='appointments',
    )
    date = models.DateField()
    time = models.TimeField()
    phone = models.CharField(max_length=20, blank=True)
    reason = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient_name} - {self.department}'
