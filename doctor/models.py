from django.db import models


class Doctor(models.Model):
    image = models.ImageField(upload_to='doctor_images/', blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], default='male')
    specialization = models.CharField(max_length=100)
    department = models.ForeignKey(
        'department.Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='doctors',
    )
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    present_address = models.CharField(max_length=255, blank=True)
    permanent_address = models.CharField(max_length=255, blank=True)
    education = models.CharField(max_length=255, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    wage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    contract_start = models.DateField(null=True, blank=True)
    contract_end = models.DateField(null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return ' '.join(part for part in (self.first_name, self.last_name) if part)

    def __str__(self):
        return self.full_name


class DoctorSchedule(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['day_of_week', 'start_time']

    def __str__(self):
        return f'{self.doctor.full_name} - {self.get_day_of_week_display()} ({self.start_time}-{self.end_time})'
